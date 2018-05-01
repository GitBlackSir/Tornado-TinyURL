# -*- coding:UTF-8 -*-
# __Auth__  : @GitBlackSir
# __Date__  : 2018/4/25
# __Email__ : gitblacksir@gmail.com

def usage():
    print\
    (
    ' -h [--help]             查看指令信息 \n'
    ' -m [--mysql]            orm初始化process_address表\n'
    ' -l [--list]             查看已注册的服务器信息 \n'
    ' -i [--ip=ADDRESS]       default=localhost\n' 
    ' -p [--port=PORT]        default=1104\n' 
    ' -d [--datacenter=DC_ID] default=0\n' 
    ' -W [--worker=WORKER_ID] default=0\n'
    )