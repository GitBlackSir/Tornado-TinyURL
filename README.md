## [龙卷风·短网址Beta](http:tinyurl.1024bit.io)

### Environment
- `Python3.6` `Tornado5` `SQLAlchemy` `Redis` `MySQL`

```
$ screen python3.6 server_api_for_develop.py --port=1111 --datacenter=0 --worker==0 &
$ screen python3.6 server_api_for_user.py -- port=2222 &
$ screen python3.6 server_web.py &
$ screen python3.6 server_redirct.py &
```

### Docker
- Coding...Dockerfile

---

## API Reference

### http://api-id.1024bit.io/

**返回`Json`示例:**

```
json = {
	"status": 0
	"messages": "SUCCESSFUL!"
	"id": 4088633170486886401,
	"short_url": "4S1YXNt1JN7",
	"time": 1525087710.975234,
	"data_center_id": 0,
	"worker_id": 0,
}
```

> -  "status":
>	- 0 `请求成功`
>		- messages": "SUCCESSFUL!"
>		- "id": 0 `由分布式发号器计算出的`64bit`整数`
> 		- "short_url": "http://t.1024bit.io/4S5zsUzQOlj" `64bit整数转62进制[0-9a-zA-Z]字符串`
>		- "time": 1525087234.847292 `unix当前时间戳`毫秒`
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

### http://api-url.1024bit.io/json&convert=`URL`

`URL`:所需转换的长网址

**返回`Json`示例:**

```
json = {
	"status": 3,
	"messages": "SUCCESSFUL SHORT_URL FROM API_DEVELOP!",
	"short_url": "http://t.1024bit.io/4S5A2O6o9wZ"
}
```
> - "status":
>	- 0 "messages": "EMPTY URL!","short_url": None
>	- 1 "messages": "FORBID INPUT TINYURL!","short_url": None
>	- 2 "messages": "SUCCESSFUL SHORT_URL FROM REDIS!","short_url": "http://t.1024bit.io/xxxxx"
>	- 3 "messages": "SUCCESSFUL SHORT_URL FROM API_DEVELOP!","short_url": "http://t.1024bit.io/xxxxx"
>	- 4 "messages": "URL INPUT ERROR!","short_url": None
>	- 5 "messages": "URL ERROR!","short_url": None

---

### http://api-url.1024bit.io/json&restore=`URL`

`URL`:所需转换的短网址

**返回`Json`示例:**

```
json = {
	"status": 1,
	"messages": "SUCCESSFULL!",
	"long_url": "https://www.google.com/ncr"
}
```
> - "status":
>	- 0 "messages": "EMPTY URL!","long_url": None
> 	- 1 "messages": "SUCCESSFULL!","long_url":"http://google.com/ncr"
> 	- 2 "messages": "URL ERROR! EG:http://t.1024bit.io/+xxxxx","long_url": None
>	- 3 "messages": "URL ERROR!","long_url": None
>	- 4 "messages": "URL ERROR!","long_url": None



