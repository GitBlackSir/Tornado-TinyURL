# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/27
# __Email__ : gitblacksir@gmail.com

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#id_server
EPOCH_TIMESTAMP     = 550281600000
ADDRESS             = '0.0.0.0'
R_ADDRESS           = '0.0.0.0'
PORT                = 1104
DC_ID               = 0
WORKER_ID           = 0

#tornado
tornado_web_port    = 8888
tornado_server_port = 8889

#mysql-------------------------------------------------------
mysql_user          = 'user'
mysql_password      = 'password'
mysql_host          = '0.0.0.0'
mysql_port          = '3306'
mysql_db_name       = 'DB'
mysql_tb_name       = 'TB'
mysql_engine        = create_engine('mysql+mysqlconnector://' +
                             mysql_user +
                             ':' + mysql_password +
                             '@' + mysql_host +
                             ':' + mysql_port +
                             '/' + mysql_db_name)

mysql_conn          = mysql_engine.connect()
mysql_DBSession      = sessionmaker(bind=mysql_engine)

#redis-------------------------------------------------------
import redis
by_redis            = redis.Redis(host='0.0.0.0', port=1111,db=0)

#client-------------------------------------------------------
id_server_host      = '0.0.0.0'
id_server_port      = 1104