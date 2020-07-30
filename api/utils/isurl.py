# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

import tornado.gen
import tornado.httpclient
from tornado import gen

@gen.coroutine
def isurl(url):
    try:
        AsyncHTTPClient = tornado.httpclient.AsyncHTTPClient()
        resp = yield AsyncHTTPClient.fetch(url, request_timeout=0.4)
        AsyncHTTPClient.close()
        return True if resp.code == 200 else False
    except:
        return False