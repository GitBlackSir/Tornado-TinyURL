# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

from tornado.web import url
from demo.web.controller import web_Handler

handlers = {
    url(r"/", web_Handler.HomeHandler, name="index"),
    url(r"/restore", web_Handler.RestoreHandler, name="restore"),
    url(r"/anonymous", web_Handler.AnonymousHandler, name="anonymous"),
    url(r"/api", web_Handler.ApiHandler, name="api"),
    url(r"/blog", web_Handler.BlogHandler, name="blog"),
}