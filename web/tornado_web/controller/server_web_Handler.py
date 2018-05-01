# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import json
import web.tornado_web.models.client as client

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
            if self.get_argument('dat',None):
                dict = (client.Client('127.0.0.1','2222',str(self.get_argument('dat',None))).get_tinyurl())
                print(dict)
                if dict['short_url']:
                    data = {'status': 1, 'messages': 'erro', 'data': [dict['short_url'], ]}
                    self.write(json.dumps(data))
                else:
                    data = {'status': 0, 'messages': 'erro', 'data': [dict['messages'], ]}
                    self.write(json.dumps(data))
class RestoreHandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.render("restore.html")

    def post(self):
        if self.get_argument('dat', None):
            dict = (client.Client('127.0.0.1', '2222', str(self.get_argument('dat', None))).get_longurl())
            if dict['long_url']:
                data = {'status': 1, 'messages': 'erro', 'data': [dict['long_url'], ]}
                self.write(json.dumps(data))
            else:
                data = {'status': 0, 'messages': 'erro', 'data': [dict['messages'], ]}
                self.write(json.dumps(data))

class AnonymousHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("anonymous.html")

class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("api.html")

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://1024bit.io')

