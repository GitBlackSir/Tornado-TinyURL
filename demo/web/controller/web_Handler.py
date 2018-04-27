# -*- coding: utf-8 -*-
# __Auth__  : Blacksir.cn
# __Date__  : 2017/12/14.
# __Email__ : gitblacksir@gmail.com

import tornado.web
import json
from conf import by_redis
from demo.web.models.client import get_guid
from demo.web.models.is_true_url import is_url
from src.base62 import _62to_10Base

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        try:
            long_url = self.get_argument("dat", None)  # 此处的'dat'对应ajax里的data:{dat:temp}的dat,即字典的键
            if long_url == '':
                data = {'status': 1, 'message': 'erro', 'data': ['请输入网址！', ]}
                self.write(json.dumps(data))
            else:
                str = is_url(long_url)
                if str:
                    if by_redis.get(long_url):
                        short_url = by_redis.get(long_url).decode()
                        print(short_url)
                        data = {'status': 0, 'message': 'successfully', 'data': ['http://t.1024bit.io/' + short_url, ]}
                    else:
                        id_url_dict = get_guid()
                        print(id_url_dict)
                        by_redis.set(id_url_dict['id'],long_url)
                        by_redis.set(long_url,id_url_dict['short_url'])
                        data = {'status': 0, 'message': 'successfully', 'data': ['http://t.1024bit.io/'+ id_url_dict['short_url'], ]}  # 封装数据
                    self.write(json.dumps(data))
                else:
                    data = {'status': 1, 'message': 'erro', 'data': ['网址不存在 请重新输入！', ]}
                    self.write(json.dumps(data))
                    # 调用json将数据格式化，使用write方法把数据传回到ajax在success情况下的的arg参数里
        except:
            print('长网址压缩未知错误...')

class RestoreHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("restore.html")

    def post(self):
        try:
            short_html_url = self.get_argument("dat", None)  # 此处的'dat'对应ajax里的data:{dat:temp}的dat,即字典的键
            if short_html_url == '':
                data = {'status': 1, 'message': 'erro', 'data': ['请输入网址！', ]}
                self.write(json.dumps(data))
            else:
                str = is_url(short_html_url)
                if str:
                    try:
                        short_html_url = short_html_url.split('/')
                        print(short_html_url[3])
                        short_url_id = _62to_10Base(short_html_url[3])
                        data = by_redis.get(short_url_id).decode()
                        data = {'status': 0, 'message': 'successfully', 'data': [data, ]}
                        self.write(json.dumps(data))
                    except:
                        data = {'status': 1, 'message': 'successfully', 'data': ['短网址格式错误\n例:http://t.1024bit.io/+ 短后缀', ]}
                        self.write(json.dumps(data))
                else:
                    data = {'status': 1, 'message': 'erro', 'data': ['短网址不存在 请重新输入！', ]}
                    self.write(json.dumps(data))
        except:
            print('短网址还原未知错误...')

class AnonymousHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("anonymous.html")

class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("api.html")

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://1024bit.io')

