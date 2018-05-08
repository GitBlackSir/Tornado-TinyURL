## API `Demo`：[龙卷风·短网址Beta](http://tinyurl.1024bit.io)

### Environment
- [`源码 GitHub`](https://github.com/GitBlackSir/Tornado_TinyURL.git)
- `Python3.6` `Tornado5` `SQLAlchemy` `Redis` `MySQL`
- 运行`run_api_server.py`附加参数`--help`查看脚本命名说明

```
$ python3.6 run_api_server --help
```
- 分别执行`API`服务端与`Demo``龙卷风·短网址Web系统`

```
$ screen python3.6 run_api_server.py --port=1104 --datacenter=0 --worker=0 &

$ screen python3.6 run_web_server.py &
```

### Docker
- Coding...Dockerfile

---

## API Reference

### http://tinyurl-api.1024bit.io/json&get-id-url

**返回`Json`示例:**

```
json = {
	"status": 0,
	"messages": "SUCCESSFUL!",
	"id": 4091465116246081537,
	"short_url": "4SeX7N2RNYt",
	"time": 1525762899.459599,
	"data_center_id": 0,
	"worker_id": 0,
}
```

> -  "status":
>	- 0 `请求成功`
>		- messages": "SUCCESSFUL!"
>		- "id":  4091465116246081537, `由分布式发号器计算出的64bit整数`
> 		- "short_url": "4SeX7N2RNYt", `64bit整数转62进制[0-9a-zA-Z]字符串`
>		- "time": 1525762899.459599, `unix当前时间戳毫秒`
>		- "data_center_id":0 `分布式进程所在数据中心集群ID`
> 		- "worker_id":0 `分布式进程所在工作机器，可理解进为程标识码ID`
>	- 1 `请求失败`
>		- messages": "ERROR!"
>		- "id": None
> 		- "short_url": None
>		- "time": 1525087234.847292
>		- "data_center_id":0
> 		- "worker_id":0


---

### http://tinyurl-api.1024bit.io/json&convert=`URL`

`URL`:所需转换的长网址

**返回`Json`示例:**

```
json = {
	"status": 3,
	"messages": "SUCCESSFUL SHORT_URL FROM API!",
	"short_url": "http://t.1024bit.io/4SeXcf5cBsl"
}
```
> - "status":
>	- 0 "messages": "EMPTY URL!","short_url": None
>	- 1 "messages": "FORBID INPUT TINYURL!","short_url": None
>	- 2 "messages": "SUCCESSFUL SHORT_URL FROM REDIS!","short_url": "http://t.1024bit.io/4SeXcf5cBsl"
>	- 3 "messages": "SUCCESSFUL SHORT_URL FROM API!","short_url": "http://t.1024bit.io/4SeXcf5cBsl"
>	- 4 "messages": "URL INPUT ERROR!","short_url": None
>	- 5 "messages": "URL ERROR!","short_url": None

---

### http://tinyurl-api.1024bit.io/json&restore=`URL`

`URL`:所需转换的短网址

**返回`Json`示例:**

```
json = {
	"status": 1,
	"messages": "SUCCESSFULL!",
	"long_url": "https://aceld.gitbooks.io/libevent/content/"
	}
```
> - "status":
>	- 0 "messages": "EMPTY URL!","long_url": None
> 	- 1 "messages": "SUCCESSFULL!","long_url":"http://google.com/ncr"
> 	- 2 "messages": "URL ERROR! http://t.1024bit.io/+xxxxx","long_url": None
>	- 3 "messages": "URL ERROR!","long_url": None
>	- 4 "messages": "URL ERROR!","long_url": None

---

## API Client For Python

`请求示例 `

```
for i in range(100):
    print(Client('tinyurl-api.1024bit.io',80).get_id())
```
```
import json
import requests
class Client(object):
    def __init__(self, host, port, url = ''):
        self.url = url
        self.host = host
        self.port = port
        self.api_develop = 'http://%s:%s/json&get-id-url' % (self.host, self.port)
        self.api_user_get_tinyurl = 'http://%s:%s/json&convert=%s/' %(self.host,self.port,self.url)
        self.api_user_get_longurl = 'http://%s:%s/json&restore=%s/' %(self.host,self.port,self.url)

    def get_id(self):
        res = requests.get(self.api_develop)
        return json.loads(res.text)

    def get_tinyurl(self):
        res = requests.get(self.api_user_get_tinyurl)
        return json.loads(res.text)
    def get_longurl(self):
        res = requests.get(self.api_user_get_longurl)
        return json.loads(res.text)

```
