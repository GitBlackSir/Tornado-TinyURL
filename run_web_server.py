# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import tornado.ioloop
from src.web.tornado_conf import server_web_tornado_config,server_web_tornado_url_mapping
from src.api.conf import api_config

def make_app():
    return tornado.web.Application(server_web_tornado_url_mapping.handlers, **server_web_tornado_config.web_server_settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(api_config.web_port)
    print('http://localhost:' + str(api_config.web_port))
    tornado.ioloop.IOLoop.current().start()