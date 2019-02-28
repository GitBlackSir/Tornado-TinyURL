# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import json
import tornado.httpclient
import tornado.gen
import tornado.escape
from src.api.conf import api_config

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    @tornado.gen.coroutine
    def post(self):
        http = tornado.httpclient.AsyncHTTPClient()
        try:
            if self.get_argument('dat',None):
                print(str(self.get_argument('dat', None)))
                response = yield http.fetch(api_config.api['ADDRESS']+":"+str(api_config.api['PORT'])+"/json&convert="+str(self.get_argument('dat',None)))
                # dict = (client.Client('127.0.0.1','8888',str(self.get_argument('dat',None))).get_tinyurl())
                dict = tornado.escape.json_decode(response.body)
                print(dict)
                if dict['short_url']:
                    data = {'status': 0, 'messages': 'erro', 'data': [dict['short_url'], ]}
                    self.write(json.dumps(data))
                else:
                    data = {'status': 1, 'messages': 'erro', 'data': [dict['messages'], ]}
                    self.write(json.dumps(data))
        except:
            data = {'status': 2, 'messages': 'erro', 'data': ['URL ERROR!', ]}
            self.write(json.dumps(data))

class RestoreHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        if self.get_argument('dat', None):
            try:
                http = tornado.httpclient.AsyncHTTPClient()
                response = yield http.fetch(api_config.api['ADDRESS']+":"+str(api_config.api['PORT'])+"/json&restore=" + str(self.get_argument('dat', None)))
                dict = tornado.escape.json_decode(response.body)
                # dict = (client.Client('127.0.0.1', '8888', str(self.get_argument('dat', None))).get_longurl())
                print(dict)
                if dict['long_url']:
                    data = {'status': 0, 'messages': 'erro', 'data': [dict['long_url'], ]}
                    self.write(json.dumps(data))
                else:
                    data = {'status': 1, 'messages': 'erro', 'data': [dict['messages'], ]}
                    self.write(json.dumps(data))
            except:
                data = {'status': 2, 'messages': 'erro', 'data': ['URL ERROR!', ]}
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
        self.redirect("http://blog.1024bit.io/blog/2018/05/01/%E5%9F%BA%E4%BA%8E%E5%88%86%E5%B8%83%E5%BC%8FID%E5%8F%91%E5%8F%B7%E5%99%A8%E7%9A%84%E7%9F%AD%E7%BD%91%E5%9D%80%E7%B3%BB%E7%BB%9FAPI%E8%AF%B4%E6%98%8E/")

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://blog.1024bit.io')

