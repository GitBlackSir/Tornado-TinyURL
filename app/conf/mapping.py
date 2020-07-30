# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import sys
sys.path.append('../')

from tornado.web import url
from handler.MainHandler import MainHandler

mapping = { url(r"/", MainHandler) }

    # url(r"/restore", WebServerHandler.RestoreHandler, name="restore"),
    # url(r"/api", WebServerHandler.ApiHandler, name="api"),
    # url(r"/blog", WebServerHandler.BlogHandler, name="blog"),
# }