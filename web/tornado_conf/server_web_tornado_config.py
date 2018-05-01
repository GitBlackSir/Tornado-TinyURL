# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

web_server_settings = dict(
    template_path     = './web/tornado_web/template/',
    static_path       = './web/tornado_web/static/',
    cookie_secret     ="4=NDnIdasDPCus/aUASLNdlasSIQWOoa/sdja=",
    login_url         ="/login",
    xsrf_cookies      =False,
    debug             =True,
)

redirct_server_settings = dict(
    cookie_secret     ="asdasdsdf=asd12dasASDADAS",
    xsrf_cookies      =False,
    debug             =True,
)
