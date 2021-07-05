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
app = Mask(__name__)


app.config["REDIS_PREFIX"] = "TEST:"
app.config["REDIS_URL"] = "redis://:password@ip:port/db"

# Example with multi redis databases
app.config["REDIS_BINDS"] = {
    "DEFAULT": {
        "REDIS_URL": "xxx"
    }, 
    "rds-01": {
        "REDIS_URL": "xxx"
    }
}

redis.init_app(app)


@app.route(method="SayHello", service="Hello")
def say_hello_handler(request: HelloRequest) -> HelloResponse:
    user_desc = redis.get(f"User:Desc:{request.name}")
    return HelloResponse(message=user_desc)


if __name__ == "__main__":
    app.run(port=10086)
```

### Configuration

A list of configuration keys currently understood by the extensions:

| Key  | Desc |
| ---- | ---- |
| REDIS_PREFIX | Storage key prefix |
| REDIS_URL | Default redis bind url |
| REDIS_BINDS | Bind multi redis databases  |


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

### Coffee

Please give me a cup of coffee, thank you!

BTC: 1657DRJUyfMyz41pdJfpeoNpz23ghMLVM3

ETH: 0xb098600a9a4572a4894dce31471c46f1f290b087

### Links

* Release: https://github.com/Eastwu5788/Mask-Redis/releases
* Code: https://github.com/Eastwu5788/Mask-Redis
* Issue tracker: https://github.com/Eastwu5788/Mask-Redis/issues
