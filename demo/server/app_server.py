# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import tornado.ioloop
from demo.conf import tornado_config,app_server_url_mapping
import conf

def make_app():
    return tornado.web.Application(app_server_url_mapping.handlers, **tornado_config.settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(conf.tornado_server_port)
    print('http://localhost:' + str(conf.tornado_server_port))
    tornado.ioloop.IOLoop.current().start()
