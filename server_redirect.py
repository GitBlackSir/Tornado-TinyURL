# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import tornado.ioloop
from web.tornado_conf import server_web_tornado_config,server_redirct_tornado_url_mapping
import conf.conf as conf

def make_app():
    return tornado.web.Application(server_redirct_tornado_url_mapping.handlers, **server_web_tornado_config.redirct_server_settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(conf.tornado_redirct_port)
    print('http://localhost:' + str(conf.tornado_redirct_port))
    tornado.ioloop.IOLoop.current().start()
