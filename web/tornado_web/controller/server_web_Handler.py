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
        try:
            if self.get_argument('dat',None):
                dict = (client.Client('127.0.0.1','2222',str(self.get_argument('dat',None))).get_tinyurl())
                print(dict)
                if dict['short_url']:
                    data = {'status': 0, 'messages': 'erro', 'data': [dict['short_url'], ]}
                    self.write(json.dumps(data))
                else:
                    data = {'status': 1, 'messages': 'erro', 'data': [dict['messages'], ]}
                    self.write(json.dumps(data))
        except:
            data = {'status': 2, 'messages': 'erro', 'data': ['API_USER ERROR!', ]}
            self.write(json.dumps(data))

class RestoreHandler(tornado.web.RequestHandler):
    def post(self):
        if self.get_argument('dat', None):
            try:
                dict = (client.Client('127.0.0.1', '2222', str(self.get_argument('dat', None))).get_longurl())
                print(dict)
                if dict['long_url']:
                    data = {'status': 0, 'messages': 'erro', 'data': [dict['long_url'], ]}
                    self.write(json.dumps(data))
                else:
                    data = {'status': 1, 'messages': 'erro', 'data': [dict['messages'], ]}
                    self.write(json.dumps(data))
            except:
                data = {'status': 2, 'messages': 'erro', 'data': ['API_USER ERROR!', ]}
                self.write(json.dumps(data))

# class BaseHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write_error(404)
#     def write_error(self, status_code, **kwargs):
#         if status_code == 404:
#             self.redirect("http://1024bit.io/blog/2018/05/01/基于分布式发号器的短网址系统API-Reference/")
#         elif status_code == 500:
#             self.render('public/500.html')
#         else:
#             self.write('error:' + str(status_code))
# class AnonymousHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("anonymous.html")

class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("http://1024bit.io/blog/2018/05/01/基于分布式发号器的短网址系统API-Reference/")

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://1024bit.io')

