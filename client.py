# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/30
# __Email__ : gitblacksir@gmail.com

import json
import requests
import conf.conf as conf
class Client(object):
    def __init__(self, host, port, url = ''):
        self.url = url
        self.host = host
        self.port = port
        self.api_develop = 'http://%s:%s/' % (self.host, self.port)
        self.api_user_get_tinyurl = 'http://%s:%s/json&convert=%s/' %(self.host,self.port,self.url)
        self.api_user_get_longurl = 'http://%s:%s/json&restore=%s/' %(self.host,self.port,self.url)

    def get_develop_json(self):
        res = requests.get(self.api_develop)
        return json.loads(res.text)

    def get_develop_status_json(self):
        res = requests.get(self.api_develop + 'stats')
        return json.loads(res.text)

    def get_tinyurl(self):
        res = requests.get(self.api_user_get_tinyurl)
        return json.loads(res.text)
    def get_longurl(self):
        res = requests.get(self.api_user_get_longurl)
        return json.loads(res.text)

develop_client = Client(conf.server_api_for_develop['ADDRESS'], conf.server_api_for_develop['PORT'])

def setup(host, port):
    global develop_client
    develop_client = Client(host, port)

def get_guid():
    return develop_client.get_develop_json()

def get_stats():
    return develop_client.get_develop_status_json()