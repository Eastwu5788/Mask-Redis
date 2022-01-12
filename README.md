## Mask-Redis

`Redis` extension for `Mask` .

### Install

`Mask-Redis` support pypi packages, you can simply install by:

```
pip install mask-redis
```

### A Simple Example

This is very easy to use `Mask-Redis` in your project.

```
from mask import Mask
from mask_redis import Redis
from examples.protos.hello_pb2 import HelloRequest, HelloResponse


redis = Redis()
app = Flask(__name__)

app.config["REDIS_PREFIX"] = "EG:"
app.config["REDIS_URL"] = "redis://:password@host:port/db"
app.config["REDIS_DECODE_RESPONSES"] = True
redis.init_app(app)


@app.route(method="SayHello", service="Hello")
def say_hello_handler(request: HelloRequest) -> HelloResponse:
    user_desc = redis.get(f"User:Desc:{request.name}")
    return HelloResponse(message=user_desc)


if __name__ == "__main__":
    app.run(port=10086)
```

### Multiple Databases

```
from mask import Mask
from mask_redis import Redis
from examples.protos.hello_pb2 import HelloRequest, HelloResponse


redis = Redis()
app = Flask(__name__)

app.config["REDIS_PREFIX"] = "EG:"
app.config["REDIS_BINDS"] = {
        "default": {
            "REDIS_URL": "redis://:password@host:port/db",
        },
        "DB12": {
            "REDIS_PREFIX": "EG12:",
            "REDIS_URL": "redis://:password@host:port/db",
        },
        "DB13": {
            "REDIS_PREFIX": "EG13:",
            "REDIS_URL": "redis://:password@host:port/db",
        }
}
app.config["REDIS_DECODE_RESPONSES"] = True
redis.init_app(app)


@app.route(method="SayHello", service="Hello")
def say_hello_handler(request: HelloRequest) -> HelloResponse:
    user_desc = redis["DB12"].get(f"User:Desc:{request.name}")
    return HelloResponse(message=user_desc)


if __name__ == "__main__":
    app.run(port=10086)
```

### Configuration

A list of configuration keys currently understood by the extensions:

| Key  | Desc | Example |
| ---- | ---- |  ---- |
| REDIS_PREFIX | Storage key prefix | app.config["REDIS_PREFIX"] = "EG:" |
| REDIS_URL | Default redis bind url | app.config["REDIS_BINDS"] = "redis://:pass@ip:port/db" |
| REDIS_BINDS | Bind multi redis databases  |  -- |
|REDIS_DEFAULT_BIND_KEY |        default redis bind key       |    app.config["REDIS_DEFAULT_BIND_KEY"] = "default"  |
|REDIS_CONNECTION_POOL   |      custom connection pool       |  app.config["REDIS_CONNECTION_POOL"] = ConnectionPool() |

### TIPS:

* If you don't want to use prefix on special key, you can start key with `-` to ignore prefix.
* If you use `redis.get()` or other method directly, this methods will use databases which config with  `REDIS_URL` or `DEFAULT` key in `REDIS_BINDS`*[]: 
* You can use `redis["rds-01"].get()` connect to special redis databases which config with `REDIS_BINDS`.  


### `@redis.cached()`

`Mask-Redis` support `@redis.cached` decorator to help you cache function result.

```

@redis.cached(key="User:Info:{user_id}", timeout=3600)
def query_user_info(user_id):
    return {"userId": 13, "userName": "Tony"}


user_info = query_user_info(13, cache=True)
``` 

* `cached` function will use params in function to format key.
* you can add `cache=True` or `cache=False` control whether to enable caching for this query, default is `cache=False`
* `cached` function use `json` to format structured data.


### Cluster Mode


`Flask-Redis` support redis cluster mode. There are multiple ways in which a cluster instance can be created:

Specially, `Flask-Redis` don't support multi cluster, therefore `REDIS_BINDS` is invalid for this mode.

* Using the Redis URL specification:

```python

from mask import Mask
from mask_redis import RedisCluster

app = Mask(__name__)
app.config["REDIS_DECODE_RESPONSES"] = True
app.config["REDIS_PREFIX"] = "CLU:"
app.config["REDIS_URL"] = "redis://:@127.0.0.1:7001/0"

redis = RedisCluster()
redis.init_app(app)

print(redis.get_nodes())
redis.set("K", "V")

```

* Using `host` and `port` arguments:

```python
from mask import Mask
from mask_redis import RedisCluster

app = Mask(__name__)
app.config["REDIS_DECODE_RESPONSES"] = True
app.config["REDIS_PREFIX"] = "CLU:"
app.config["REDIS_HOST"] = "127.0.0.1"
app.config["REDIS_PORT"] = "7001"

redis = RedisCluster()
redis.init_app(app)

print("redis.get_nodes()")
redis.set("K", "V")
```


Sentinel Mode
==================

`Flask-Redis` support sentinel mode. You can use a Sentinel connection to discover the master and slaves
network address. You can also create redis client connections from a sentinel instance.

```python
from mask import Mask
from mask_redis import Sentinel

app = Mask(__name__)

app.config["REDIS_PREFIX"] = "SEN:"
app.config["REDIS_SENTINELS"] = [("192.168.1.189", 18001)]
app.config["REDIS_SENTINEL_KWARGS"] = {
    "socket_timeout": 0.1
}
app.config["REDIS_CONNECTION_KWARGS"] = {
    "decode_responses": True
}

rds = Sentinel()
rds.init_app(app)

print(rds.discover_master("mymaster"))
print(rds.discover_slaves("mymaster"))

master = rds.master_for("mymaster")
slave = rds.slave_for("mymaster")

master.set("k", "v")
slave.get("k")
```


Sentinel mode is different from other simple and Cluster mode. in this mode, you should use `REDIS_SENTINELS` parameter
to config connection info. You will get details about sentinel mode parameter at below:

| Key | Docs | Example |
| ---- | ---- | ---- |
|REDIS_SENTINELS|sentinel connections|app.config["REDIS_SENTINELS"] = [("192.168.1.189", 18001)]|
|REDIS_SENTINEL_KWARGS|sentinel kwargs for Sentinel|app.config["REDIS_SENTINEL_KWARGS"] = {"socket_timeout": 0.1}|
|REDIS_CONNECTION_KWARGS|redis connection kwargs|app.config["REDIS_CONNECTION_KWARGS"] = {"decode_responses": True}|


### Coffee

Please give me a cup of coffee, thank you!

BTC: 1657DRJUyfMyz41pdJfpeoNpz23ghMLVM3

ETH: 0xb098600a9a4572a4894dce31471c46f1f290b087

### Links

* Release: https://github.com/Eastwu5788/Mask-Redis/releases
* Code: https://github.com/Eastwu5788/Mask-Redis
* Issue tracker: https://github.com/Eastwu5788/Mask-Redis/issues
