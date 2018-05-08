# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

import os
import sys
import getopt
import tornado.web
import tornado.ioloop
from src.api.conf.tornado_config import settings
from src.api.conf.tornado_url_mapping import handlers
from src.api.models.script import usage
from src.api.models import mysql_orm
from src.api.conf import api_config

import tornado.httpserver
from src.api.controller.BaseHandler import Generator

# DC_ID = api_config.api['DC_ID']
# WORKER_ID= api_config.api['WORKER_ID']

class Api_Application(tornado.web.Application):
    def __init__(self):
        self.id_generator = Generator(api_config.api['DC_ID'], api_config.api['WORKER_ID'])
        super(Api_Application, self).__init__(handlers, **settings)

if __name__ == "__main__":
    try:
        options, args = getopt.getopt(sys.argv[1:], "lhmat:p:d:w:",
                                      ['list', 'help', 'init_mysql', "api_host_name=",'tinyurl_host_name=' "port=", "datacenter=", "worker="])
        for name, value in options:
            if name in ('-h', '--help'):
                usage()
                sys.exit()
            if name in ('-l', '--list'):
                try:
                    mysql_orm.list_host_mysql()
                    sys.exit()
                except:
                    sys.exit(9)
            if name in ('-m', '--init_mysql'):
                mysql_orm.init_mysql()
                print("MYSQL建表成功！")
                print("IP:", api_config.mysql['host'])
                print("PORT:", api_config.mysql['port'])
                print("DB_NAME", api_config.mysql['db_name'])
                print("TB_NAME", api_config.mysql['tb_name'])
                sys.exit()
            elif name in ('-a', 'api_host_name='):
                api_config.api['SHORT_HOST_NAME'] = value
            elif name in ('-t', 'tinyurl_host_name='):
                api_config.api['WEB_HOST_NAME'] = value
            elif name in ('-p', '--port'):
                api_config.api['PORT'] = int(value)
            elif name in ('-d', '--datacenter'):
                api_config.api['DC_ID'] = int(value)
            elif name in ('-w', '--worker'):
                api_config.api['WORKER_ID'] = int(value)
        session = api_config.mysql_DBSession()
        session.add(mysql_orm.T(DATACENTER_ID=api_config.api['DC_ID'], PORT=api_config.api['PORT'], WORKER_ID=api_config.api['WORKER_ID'], UNIX_PID=os.getpid(), STATUS=True,SHORT_HOST_NAME =api_config.api['SHORT_HOST_NAME'],WEB_HOST_NAME=api_config.api['WEB_HOST_NAME']))
        session.commit()
        session.close()

        http_server = tornado.httpserver.HTTPServer(Api_Application())
        print("Starting ID Server start at %s:%s" % (api_config.api['ADDRESS'],api_config.api['PORT']))
        http_server.listen(api_config.api['PORT'])
        print(os.getpid())
        tornado.ioloop.IOLoop.instance().start()
    except:
        pass
    finally:
            session = api_config.mysql_DBSession()
            session.query(mysql_orm.T).filter(mysql_orm.T.UNIX_PID == os.getpid(),
                                             mysql_orm.T.DATACENTER_ID == api_config.api['DC_ID'],
                                             mysql_orm.T.WORKER_ID == api_config.api['WORKER_ID']).update({mysql_orm.T.STATUS:False})
            session.commit()
            session.close()