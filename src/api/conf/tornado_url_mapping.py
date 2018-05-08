# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

from tornado.web import url
from src.api.controller.BaseHandler import IDHandler,StatsHandler,Api_Long_To_Short_URL_Handler,Api_Short_To_Long_URL_Handler,TinyURL_RedirctHandler

handlers = {
    url(r'/json&get-id-url', IDHandler),
    url(r'/json&get-stats', StatsHandler),
    url(r'/json&convert=(.*)', Api_Long_To_Short_URL_Handler),
    url(r'/json&restore=(.*)', Api_Short_To_Long_URL_Handler),
    url(r"/([a-zA-Z0-9]+$)", TinyURL_RedirctHandler),
}