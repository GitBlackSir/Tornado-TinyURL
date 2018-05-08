# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

from tornado.web import url
from src.web.tornado_web.controller import server_web_Handler

handlers = {
    url(r"/", server_web_Handler.HomeHandler, name="index"),
    url(r"/restore", server_web_Handler.RestoreHandler, name="restore"),
    url(r"/api", server_web_Handler.ApiHandler, name="api"),
    url(r"/blog", server_web_Handler.BlogHandler, name="blog"),
}