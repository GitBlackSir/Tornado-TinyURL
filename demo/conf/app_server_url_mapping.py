# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

from tornado.web import url
from demo.server.controller.server_Handler import server_HomeHandler,server_RedirctHandler

handlers = {
    url(r"/",server_HomeHandler),
    url(r"/([a-zA-Z0-9]+$)", server_RedirctHandler),

}