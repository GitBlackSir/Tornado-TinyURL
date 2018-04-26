# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/25
# __Email__ : gitblacksir@gmail.com

import requests
import json

class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.api_uri = 'http://%s:%s/' % (self.host, self.port)
    def get_guid(self):
        res = requests.get(self.api_uri)
        return int(res.text)
    def get_stats(self):
        res = requests.get(self.api_uri + 'stats')
        return json.loads(res.text)

default_client = Client('localhost', 1234)
def setup(host, port):
    global default_client
    default_client = Client(host, port)
def get_guid():
    return default_client.get_guid()
def get_stats():
    return default_client.get_stats()

