# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
from src.base62 import _62to_10Base
import conf.conf as conf
import client as client

class server_HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://tinyurl.1024bit.io/')

class server_RedirctHandler(tornado.web.RequestHandler):
    def get(self,data):
        try:
            if data:
                print(data)
                dict = client.Client('127.0.0.1','2222',"http://t.1024bit.io/"+data).get_longurl()
                self.redirect(dict['long_url'])
            else:
                self.redirect('http://tinyurl.1024bit.io/')
        except:
            self.redirect('http://tinyurl.1024bit.io/')
