# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/25
# __Email__ : gitblacksir@gmail.com

import os
import sys
import json
import time
import getopt
import tornado.web
import tornado.ioloop
import tornado.httpserver
import logging.config
import by_usage as by_usage
import by_mysql as by_mysql
import by_base62 as by_base62
import conf

EPOCH_TIMESTAMP = 550281600000
ADDRESS = '127.0.0.1'
R_ADDRESS = '127.0.0.1'
PORT=1104
DC_ID=0
WORKER_ID=0

class Generator(object):
    def __init__(self, dc, worker):
        self.dc = dc
        self.worker = worker
        self.node_id = ((dc & 0x03) << 8) | (worker & 0xff)
        self.last_timestamp = EPOCH_TIMESTAMP
        self.sequence = 0
        self.sequence_overload = 0
        self.errors = 0
        self.generated_ids = 0

    def get_next_id(self):
        curr_time = int(time.time() * 1000)

        if curr_time < self.last_timestamp:
            # stop handling requests til we've caught back up
            self.errors += 1
            raise tornado.web.HTTPError(500,
                                        'Clock went backwards! %d < %d' % (curr_time, self.last_timestamp))

        if curr_time > self.last_timestamp:
            self.sequence = 0
            self.last_timestamp = curr_time

        self.sequence += 1

        if self.sequence > 4095:
            # the sequence is overload, just wait to next sequence
            logging.warning('The sequence has been overload')
            self.sequence_overload += 1
            time.sleep(0.001)
            return self.get_next_id()

        generated_id = ((curr_time - EPOCH_TIMESTAMP) << 22) | (self.node_id << 12) | self.sequence

        self.generated_ids += 1
        return generated_id

    @property
    def stats(self):
        return {
            'dc': self.dc,
            'worker': self.worker,
            'timestamp': int(time.time() * 1000),  # current timestamp for this worker
            'last_timestamp': self.last_timestamp,  # the last timestamp that generated ID on
            'sequence': self.sequence,  # the sequence number for last timestamp
            'sequence_overload': self.sequence_overload,
        # the number of times that the sequence is overflow
            'errors': self.errors,  # the number of times that clock went backward
        }

class IDHandler(tornado.web.RequestHandler):
    def get(self):
        generated_id = self.application.id_generator.get_next_id()
        self.set_header("Content-Type", "application/json")
        id_url_json = {'id':generated_id,'short_url':by_base62._10to_62Base(generated_id)}
        self.write(id_url_json)
        # self.write(str(generated_id))
        self.flush()  # avoid ETag, etc generation

class StatsHandler(tornado.web.RequestHandler):
    def get(self):
        stats = self.application.id_generator.stats
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(stats))

class SnowflakeApplication(tornado.web.Application):
    def __init__(self, **settings):
        handlers = [
            (r'/', IDHandler),
            (r'/stats', StatsHandler),
        ]
        settings = {
            'debug': False,
        }
        self.id_generator = Generator(DC_ID, WORKER_ID)
        super(SnowflakeApplication, self).__init__(handlers, **settings)

if __name__ == '__main__':
    try:
        options, args = getopt.getopt(sys.argv[1:], "lhmi:p:d:w:",
                                      ['list', 'help', 'init_mysql' "ip=", "port=", "datacenter=", "worker="])
        for name, value in options:
            if name in ('-h', '--help'):
                by_usage.usage()
                sys.exit()
            if name in ('-l', '--list'):
                by_mysql.list_host_mysql()
                sys.exit()
            if name in ('-m', '--init_mysql'):
                by_mysql.init_mysql()
                print("MYSQL建表成功！")
                print("IP:", conf.host)
                print("PORT:", conf.port)
                print("DB_NAME", conf.db_name)
                print("TB_NAME", conf.tb_name)
                sys.exit()

            elif name in ('-i', '--ip'):
                R_ADDRESS = value
            elif name in ('-p', '--port'):
                PORT = int(value)
            elif name in ('-d', '--datacenter'):
                DC_ID = int(value)
            elif name in ('-w', '--worker'):
                WORKER_ID = int(value)
        session = conf.DBSession()
        session.add(by_mysql.T(datacenter_id=DC_ID, port=PORT, worker_id=WORKER_ID, unix_pid=os.getpid(), status=True))
        session.commit()
        session.close()

            # setup logging
        logging.config.fileConfig(os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            'logging.ini',
        )))
        http_server = tornado.httpserver.HTTPServer(SnowflakeApplication())
        print("Starting ID Server start at %s:%d" % (ADDRESS, PORT))
        http_server.listen(PORT,ADDRESS)
        try:
            print(os.getpid())
            tornado.ioloop.IOLoop.instance().start()
        finally:
            session = conf.DBSession()
            session.query(by_mysql.T).filter(by_mysql.T.unix_pid == os.getpid(),
                                             by_mysql.T.datacenter_id == DC_ID,
                                             by_mysql.T.worker_id == WORKER_ID).update({by_mysql.T.status:False})
            session.commit()
            session.close()
        # except Exception:
        #     logging.exception('Server error')
    except getopt.GetoptError:
        by_usage.usage()