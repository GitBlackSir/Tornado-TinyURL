---
layout: post
title: 这里是题目
tags:
- 标签1
- 标签2
categories: 分类
description: 描述。
---

[TOC]

# 基于分布式发号器的短网址系统接口

`演示网址:`[龙卷风·短网址Beta](http://tinyurl.1024bit.io) 
## PROJECT
### Environment 
- `Python3.6` `Tornado5` `SQLAlchemy` `Redis` `MySQL`

```bash
$ screen python3.6 server_api_for_develop.py --port=1111 --datacenter=0 --worker==0 &
$ screen python3.6 server_api_for_user.py -- port=2222 &
$ screen python3.6 server_web.py &
$ screen python3.6 server_redirct.py &
```

### Docker
- Coding...Dockerfile

## API Reference

### http://api-id.1024bit.io/

``` json
json = {
			"id": 4088633170486886401,
			"short_url": "4S1YXNt1JN7",
			"time": 1525087710.975234,
			"data_center_id": 0,
			"worker_id": 0,
			"status": 1
}

/*说明
	id：基于分布式发号器的64bit整数
	short_url：由64bit转为[0-9a-zA-Z]的62进制字符串短网址后缀
	time：获取当前unix时间
	data\_center_id：当前分布式进程集群
	worker_id：当前分布式进程所在机器（也可以理解为进程标识码）
	status:
					0: '请求失败'
					1: '请求成功'
*/
```


### http://api-url.1024bit.io/json&convert=`URL`
`URL`:所需转换的长网址

``` 
/*返回Json示例
json = {
		"status": 4,
		"messages": "successful",
		"short_url": "http://t.1024bit.io/4S2TAmcuSaJ"
}


/*说明 
	'status':
		0 'messages': 'EMPTY URL!','short_url': None
		1 'messages': 'FORBID INPUT TINYURL!','short_url': None
		2 'messages': 'this short_url from redis','short_url': 'http://t.1024bit.io/xxxxx'
		3 'messages': 'server api for develop successful','short_url': 'http://t.1024bit.io/xxxxx'
		4 'messages': 'URL INPUT ERRO!','short_url': None
		5 'messages': 'URL ERRO!','short_url': None
*/

```

### http://api-url.1024bit.io/json&restore=`URL`
`URL`:所需转换的短网址

```
/*返回Json示例
json = {
		"status": 1,
		"messages": "successful",
		"long_url": "https://www.google.com/ncr"
}


/*说明
'status':
		   0 'messages': 'messages': 'EMPTY URL!','long_url': None
		   1 'messages': 'successfully short to lang url','long_url':'http://google.com/ncr'
		   2 'messages': 'url eg:http://t.1024bit.io/+xxxxx','long_url': None
		   3 'messages': 'URL ERRO!','long_url': None
		   4 'messages': 'URL ERRO!','long_url': None
*/

```
