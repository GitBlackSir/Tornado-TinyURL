# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

import tornado.web
import time
import json
from src.api.models import true_url, base62
import src.api.conf.api_config as api_config
import tornado.httpclient
import tornado.gen
import tornado.escape

EPOCH_TIMESTAMP = api_config.api['EPOCH_TIMESTAMP']

class Generator(object):
    def __init__(self, dc, worker):
        global DC_ID,WORKER_ID
        DC_ID = dc
        WORKER_ID = worker
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
        try:
            generated_id = self.application.id_generator.get_next_id()
            self.set_header("Content-Type", "application/json")
            id_url_dict = {"status":0,"messages": "SUCCESSFUL!",'id':generated_id,'short_url': base62._10to_62Base(generated_id), "time":time.time(), "data_center_id":DC_ID, 'worker_id':WORKER_ID}
            id_url_json = json.dumps(id_url_dict)
            self.write(id_url_json)
            # self.write(str(generated_id))
            self.flush()  # avoid ETag, etc generation
        except:
            id_url_dict = {"status":1,"messages": "ERROR!",'id': None,'short_url': None,"time":time.time(),"data_center_id":DC_ID,'worker_id':WORKER_ID}
            id_url_json = json.dumps(id_url_dict)
            self.write(id_url_json)
            # self.write(str(generated_id))
            self.flush()  # avoid ETag, etc generation

class StatsHandler(tornado.web.RequestHandler):
    def get(self):
        stats = self.application.id_generator.stats
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(stats))

class Api_Long_To_Short_URL_Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self,*args):
        import json
        try:
            http = tornado.httpclient.AsyncHTTPClient()
            self.set_header("Content-Type", "application/json")
            if args[0] == '':
                dict = {'status':0,'messages':'EMPTY URL!', 'short_url': None}
                self.write(json.dumps(dict))
                self.flush()  # avoid ETag, etc generation
            elif args[0].split("/")[2] == api_config.api['SHORT_HOST_NAME'].split("/")[2]:
                dict = {'status':1,'messages':'FORBID INPUT TINYURL!','short_url':None }
                self.write(json.dumps(dict))
                self.flush()  # avoid ETag, etc generation
            else:
                if true_url.is_url(args[0]):
                    if api_config.redis_conn.get(args[0]):
                        dict = {'status':2, 'messages':'SUCCESSFUL SHORT_URL FROM REDIS!', 'short_url': api_config.api['SHORT_HOST_NAME'] + api_config.redis_conn.get(args[0]).decode(), }
                        self.write(json.dumps(dict))
                        self.flush()  # avoid ETag, etc generation
                    else:
                        response = yield http.fetch(api_config.api['ADDRESS']+":"+str(api_config.api['PORT'])+"/json&get-id-url")
                        id_url_dict = tornado.escape.json_decode(response.body)
                        api_config.redis_conn.set(id_url_dict['short_url'], args[0])
                        api_config.redis_conn.set(args[0], id_url_dict['short_url'])
                        dict = {'status': 3, 'messages': 'SUCCESSFUL SHORT_URL FROM API!','short_url': api_config.api['SHORT_HOST_NAME'] + id_url_dict['short_url']}
                        self.write(json.dumps(dict))
                        self.flush()  # avoid ETag, etc generation
                else:
                    dict = {'status': 4, 'messages':'URL INPUT ERROR!', 'short_url':None}
                    self.write(json.dumps(dict))
                    self.flush()  # avoid ETag, etc generation
        except:
            data = {'status': 5, 'messages':'URL ERROR!','short_url':None }
            self.write(json.dumps(data))
            self.flush()  # avoid ETag, etc generation

class Api_Short_To_Long_URL_Handler(tornado.web.RequestHandler):
    def get(self,*args):
        try:
            self.set_header("Content-Type", "application/json")
            if args[0] == '':
                dict = {'status': 0, 'messages': 'EMPTY URL!', 'long_url':None}
                self.write(json.dumps(dict))
            else:
                if true_url.is_url(args[0]):
                    try:
                        print(args[0])
                        dict = {'status': 1, 'messages': 'SUCCESSFUL!', 'long_url': api_config.redis_conn.get(args[0].split('/')[3]).decode()}
                        self.write(json.dumps(dict))
                    except:
                        dict = {'status': 2, 'messages': 'URL ERROR!' + "  "+ api_config.api['SHORT_HOST_NAME'] + 'xxxxx', 'long_url': None}
                        self.write(json.dumps(dict))
                else:
                    dict = {'status': 3, 'messages': 'URL ERROR!', 'long_url': None}
                    self.write(json.dumps(dict))
        except:
            dict = {'status': 4, 'messages': 'URL ERROR!', 'long_url': None}

class TinyURL_RedirctHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self,data):
        print(data)
        try:
            self.set_header("Content-Type", "application/json")
            http = tornado.httpclient.AsyncHTTPClient()
            if data:
                print(data)
                response = yield http.fetch(api_config.api['ADDRESS']+":"+str(api_config.api['PORT'])+"/json&restore="+api_config.api['ADDRESS']+"/"+data)
                dict = tornado.escape.json_decode(response.body)
                print(dict)
                self.redirect(dict['long_url'])
            else:
                self.redirect(api_config.api['WEB_HOST_NAME'])
        except:
            self.redirect(api_config.api['WEB_HOST_NAME'])

