# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/26
# __Email__ : gitblacksir@gmail.com

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#mysql
user        = 'db_user'
password    = 'db_password'
host        = 'host_ip'
port        = 'db_port'
db_name     = 'db_name'
tb_name     = 'tb_name'
engine      = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@' + host + ':' + port + '/' + db_name)
conn        = engine.connect()
DBSession   = sessionmaker(bind=engine)