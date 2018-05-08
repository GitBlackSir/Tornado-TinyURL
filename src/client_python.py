# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/30
# __Email__ : gitblacksir@gmail.com

#Python Client客户端

import json
import requests
class Client(object):
    def __init__(self, host, port, url = ''):
        self.url = url
        self.host = host
        self.port = port
        self.api_develop = 'http://%s:%s/' % (self.host, self.port)
        self.api_user_get_tinyurl = 'http://%s:%s/json&convert=%s/' %(self.host,self.port,self.url)
        self.api_user_get_longurl = 'http://%s:%s/json&restore=%s/' %(self.host,self.port,self.url)

    def get_id(self):
        res = requests.get(self.api_develop)
        return json.loads(res.text)

    def get_tinyurl(self):
        res = requests.get(self.api_user_get_tinyurl)
        return json.loads(res.text)
    def get_longurl(self):
        res = requests.get(self.api_user_get_longurl)
        return json.loads(res.text)

# client = Client('HOST', 'PORT').get_id()