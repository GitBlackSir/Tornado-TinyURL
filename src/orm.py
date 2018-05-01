# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/25
# __Email__ : gitblacksir@gmail.com

from sqlalchemy import *
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
import conf.conf as conf

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class T(Base):
    # 表的名字:
    __tablename__ = conf.mysql_conf['tb_name']
    id = Column(Integer, primary_key=True)
    datacenter_id = Column(Integer)
    worker_id = Column(Integer)
    unix_pid = Column(Integer)
    port = Column(Integer)
    status = Column(Boolean)

def list_server():
    session = conf.mysql_DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    print(session.query(T).all())
    session.close()

def list_host_mysql():
    session = conf.mysql_DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    print('HongKong    Tencent Cloud   ---> DC_ID:0  IP:119.28.76.35')
    print('LosAngeles  Bandwagon Host  ---> DC_ID:1  IP:119.28.76.35')
    print('')
    print('{1}  {2}  {3}  {4}  {5}'.format('ID','DC_ID','WORKER_ID','PID','PORT','STATUS'))
    # print("ID DC_ID WORKER_ID  PID  PORT  STATUS")
    for row in session.query(T):
        print('{1}      {2}          {3}  {4}  {5}'.format (row.id, row.datacenter_id,row.worker_id,row.unix_pid,row.port,row.status))
    print('')
    session.close()

def init_mysql():
    metadata = MetaData(conf.mysql_engine)
    table = Table(conf.mysql_conf['tb_name'], metadata,
                  Column('id', Integer, primary_key=True),
                  Column('datacenter_id',Integer),
                  Column('worker_id', Integer),
                  Column('unix_pid', Integer),
                  Column('port', Integer),
                  Column('status', Boolean))
    metadata.create_all(conf.mysql_engine)