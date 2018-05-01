# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/27
# __Email__ : gitblacksir@gmail.com

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


server_api_for_develop = \
    {
        'EPOCH_TIMESTAMP'  :    550281600000,
        'ADDRESS'          :    '127.0.0.1',
        'R_ADDRESS'        :    '127.0.0.1',
        'PORT'             :    1111,
        'DC_ID'            :    0,
        'WORKER_ID'        :    0,
    }
server_api_for_user = \
    {
        'ADDRESS'          :    '127.0.0.1',
        'R_ADDRESS'        :    '127.0.0.1',
        'PORT'             :    2222,
    }

tornado_web_port           =    8888
tornado_redirct_port       =    8889

mysql_conf = \
    {
        'user'          : 'root',
        'password'      : '123456',
        'host'          : '127.0.0.1',
        'port'          : '3306',
        'db_name'       : 'TORNADO_TINY_URL',
        'tb_name'       : 'process_address',

    }
mysql_engine = create_engine('mysql+mysqlconnector://' +mysql_conf['user'] +':' + mysql_conf['password'] +'@' + mysql_conf['host'] +':' + mysql_conf['port'] +'/' + mysql_conf['db_name'])
mysql_conn          = mysql_engine.connect()
mysql_DBSession     = sessionmaker(bind=mysql_engine)
redis_conn          = redis.Redis(host='127.0.0.1', port=6379,db=0)

#api_client-------------------------------------------------------
server_api_host      = '127.0.0.1'
server_api_port      = '1111'