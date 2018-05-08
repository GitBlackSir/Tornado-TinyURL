# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

from sqlalchemy import *
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
import src.api.conf.api_config as api_config

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class T(Base):
    # 表的名字:
    __tablename__ = api_config.mysql['tb_name']
    ID = Column(Integer, primary_key=True)
    DATACENTER_ID = Column(Integer)
    WORKER_ID = Column(Integer)
    UNIX_PID = Column(Integer)
    PORT = Column(Integer)
    STATUS = Column(Boolean)
    SHORT_HOST_NAME = Column(String(30))
    WEB_HOST_NAME = Column(String(30))

def list_host_mysql():
        session = api_config.mysql_DBSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        print('HongKong    Tencent Cloud   ---> DC_ID:0  IP:119.28.76.35')
        print('LosAngeles  Bandwagon Host  ---> DC_ID:1  IP:119.28.76.35')
        print('')
        print('{1}  {2}  {3}  {4}  {5}'.format('ID','DC_ID','WORKER_ID','PID','PORT','STATUS'))
        # print("ID DC_ID WORKER_ID  PID  PORT  STATUS")
        for row in session.query(T).filter(T.STATUS==True):
            print('{1}      {2}          {3}  {4}  {5}'.format (str(row.ID), str(row.DATACENTER_ID),str(row.WORKER_ID),str(row.UNIX_PID),str(row.PORT),str(row.STATUS)))
        print('')
        session.close()

def init_mysql():
    metadata = MetaData(api_config.mysql_engine)
    table = Table(api_config.mysql['tb_name'], metadata,
                  Column('ID', Integer, primary_key=True),
                  Column('DATACENTER_ID',Integer),
                  Column('WORKER_ID', Integer),
                  Column('UNIX_PID', Integer),
                  Column('PORT', Integer),
                  Column('STATUS', Boolean),
                  Column('SHORT_HOST_NAME',String(30)),
                  Column('WEB_HOST_NAME', String(30)),
                  )
    metadata.create_all(api_config.mysql_engine)