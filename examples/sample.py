# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2021
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '6/30/21 9:12 AM'
from mask import Mask
from mask_redis import Redis
from examples.protos.hello_pb2 import HelloRequest, HelloResponse


redis = Redis()
app = Mask(__name__)


app.config["REDIS_PREFIX"] = "TEST:"
app.config["REDIS_URL"] = "redis://:password@ip:port/db"

redis.init_app(app)


@app.route(method="SayHello", service="Hello")
def say_hello_handler(request: HelloRequest) -> HelloResponse:
    user_desc = redis.get(f"User:Desc:{request.name}")
    return HelloResponse(message=user_desc)


if __name__ == "__main__":
    app.run(port=10086)
