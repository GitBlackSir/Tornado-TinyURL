# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/27
# __Email__ : gitblacksir@gmail.com

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

api = {
        'SHORT_HOST_NAME'  :    'http://t.1024bit.io/',
        'WEB_HOST_NAME'    :    'http://tinyurl.1024bit.io',
        'EPOCH_TIMESTAMP'  :    550281600000,
        'ADDRESS'          :    'http://127.0.0.1',
        'PORT'             :    1104,
        'DC_ID'            :    0,
        'WORKER_ID'        :    0,
}
web_port = 1103
mysql= {
        'user'          : 'user',
        'password'      : 'password',
        'host'          : '127.0.0.1',
        'port'          : '3306',
        'db_name'       : 'TORNADO_TINY_URL',
        'tb_name'       : 'process_info',
}
mysql_engine = create_engine('mysql+pymysql://' +mysql['user'] +':' + mysql['password'] +'@' + mysql['host'] +':' + mysql['port'] +'/' + mysql['db_name'])
mysql_conn          = mysql_engine.connect()
mysql_DBSession     = sessionmaker(bind=mysql_engine)
redis_conn          = redis.Redis(host='127.0.0.1', port=6666,db=0)