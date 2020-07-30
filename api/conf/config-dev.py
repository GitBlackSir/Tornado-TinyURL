# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/27
# __Email__ : gitblacksir@gmail.com

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


tornado_conf = dict(
    cookie_secret='asdasdsdf=asd12dasASDADAS',
    xsrf_cookies=False,
    debug=False
)

port = 1103

api = {
        'SHORT_HOST_NAME'  :    'http://127.0.0.1:1104/',
        'WEB_HOST_NAME'    :    'http://tinyurl.1024bit.io',
        'EPOCH_TIMESTAMP'  :     550281600000,
        'ADDRESS'          :    'http://127.0.0.1',
        'PORT'             :    1104,
        'DC_ID'            :    0,
        'WORKER_ID'        :    0,
}

mysql= {
        'user'          : 'root',
        'password'      : '123456',
        'host'          : '127.0.0.1',
        'port'          : '3306',
        'db_name'       : 'TORNADO_TINY_URL',
        'tb_name'       : 'process_info',
}

mysql_engine = create_engine('mysql+pymysql://' + mysql['user'] +':' + mysql['password'] +'@' + mysql['host'] +':' + mysql['port'] +'/' + mysql['db_name'])
mysql_conn          = mysql_engine.connect()
mysql_DBSession     = sessionmaker(bind=mysql_engine)
redis_conn          = redis.Redis(host='baiyu.com', port=6379, db=0)