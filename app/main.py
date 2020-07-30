# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import tornado.ioloop
from conf.config import port
from conf.config import config
from conf.mapping import mapping
from handler.MainHandler import MainHandler

def make_app():
    return tornado.web.Application(mapping, **config)

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    print('http://127.0.0.1:' + str(port))
    tornado.ioloop.IOLoop.current().start()