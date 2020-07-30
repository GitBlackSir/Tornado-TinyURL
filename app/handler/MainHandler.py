# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com


import json
import tornado.web
import tornado.gen
import tornado.escape
import tornado.httpclient


# class IndexHandler(tornado.web.RequestHandler):
#
#     def get(self):
#         self.render("index.html")

class MainHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def post(self):
        longURL = self.get_body_argument('longURL', strip=True)
        try:
            asynClient = tornado.httpclient.AsyncHTTPClient()
            resp = yield asynClient.fetch(str(longURL), request_timeout=0.4, validate_cert=False)
            asynClient.close()
            self.write(resp.body)
        except:
            self.write('error')
        

        # try:
        #     longURL = self.get_argument('data', None)

        #     asynClient = tornado.httpclient.AsyncHTTPClient()
        #     resp =  yield asynClient.fetch('http://www.baidu.com')

        #     if dict['short_url']:
        #         self.write(json.dumps({'code': 0, 'msg': 'success', 'data': [dict['short_url']]}))
        #     else:
        #         self.write(json.dumps({'code': 1, 'messages': 'err', 'data': [dict['messages']]}))
        # except:
        #     data = {'code': 3, 'messages': 'erro', 'data': ['URL ERROR!', ]}
        #     self.write(json.dumps(data))

# class RestoreHandler(tornado.web.RequestHandler):
#     @tornado.gen.coroutine
#     def post(self):
#         if self.get_argument('dat', None):
#             try:
#                 http = tornado.httpclient.AsyncHTTPClient()
#                 response = yield http.fetch(api_config.api['ADDRESS']+":"+str(api_config.api['PORT'])+"/json&restore=" + str(self.get_argument('dat', None)))
#                 dict = tornado.escape.json_decode(response.body)
#                 # dict = (client.Client('127.0.0.1', '8888', str(self.get_argument('dat', None))).get_longurl())
#                 print(dict)
#                 if dict['long_url']:
#                     data = {'status': 0, 'messages': 'erro', 'data': [dict['long_url'], ]}
#                     self.write(json.dumps(data))
#                 else:
#                     data = {'status': 1, 'messages': 'erro', 'data': [dict['messages'], ]}
#                     self.write(json.dumps(data))
#             except:
#                 data = {'status': 2, 'messages': 'erro', 'data': ['URL ERROR!', ]}
#                 self.write(json.dumps(data))

# class BaseHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write_error(404)
#     def write_error(self, status_code, **kwargs):
#         if status_code == 404:
#             self.redirect("http://1024bit.io/blog/2018/05/01/基于分布式发号器的短网址系统API-Reference/")
#         elif status_code == 500:
#             self.render('public/500.html')
#         else:
#             self.write('error:' + str(status_code))
# class AnonymousHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("anonymous.html")

# class ApiHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.redirect('https://blog.1024bit.io/blog/2018/05/01/%E5%9F%BA%E4%BA%8E%E5%88%86%E5%B8%83%E5%BC%8FID%E5%8F%91%E5%8F%B7%E5%99%A8%E7%9A%84%E7%9F%AD%E7%BD%91%E5%9D%80%E7%B3%BB%E7%BB%9FAPI%E8%AF%B4%E6%98%8E/')
#
# class BlogHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.redirect('https://blog.1024bit.io/')

