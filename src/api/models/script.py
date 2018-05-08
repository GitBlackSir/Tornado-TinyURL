# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

def usage():
    print(
    ' -h [--help]                                   查看指令信息\n'
    ' -m [--init_mysql]                             orm初始化process_info表\n'
    ' -l [--list]                                   查看分布式进程信息表 \n'
    ' -p [--port=PORT]                              default=1104\n' 
    ' -d [--datacenter=DC_ID]                       default=0\n' 
    ' -w [--worker=WORKER_ID]                       default=0\n'
    ' -t [--tinyurl_host_name=HOST_NAME]            default=http://tinyurl.1024bit.io\n' 
    ' -a [--api_host_name=HOST_NAME]                default=http://t.1024bit.io/\n'
)