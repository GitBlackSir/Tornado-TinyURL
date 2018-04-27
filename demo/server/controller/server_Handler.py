# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
from src.base62 import _62to_10Base
from conf import by_redis

class server_HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://tinyurl.1024bit.io/')

class server_RedirctHandler(tornado.web.RequestHandler):
    def get(self,data):
        if data:
            data = _62to_10Base(data)
            data = by_redis.get(data)
            print(data)
            self.redirect(data)
