## Mask-Redis

`Redis` extension for `Mask` .

### Install

`Mask-Redis` support pypi packages, you can simply install by:

```
pip install mask-redis
```

### Document

`Mask-Redis` manual could be found at:  https://mask-redis.readthedocs.io/en/latest


### A Simple Example

This is very easy to use `Mask-Redis` in your project.

```
from mask import Mask
from mask.parse import pre, Rule


app = Mask(__name__)



def say_hello(request, context):
    """ Handler SayHello request
    """
    return HelloResponse(message="Hello Reply: %s" % params["Name"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1020)
```



### Coffee

Please give me a cup of coffee, thank you!

BTC: 1657DRJUyfMyz41pdJfpeoNpz23ghMLVM3

ETH: 0xb098600a9a4572a4894dce31471c46f1f290b087

### Links

* Documentaion: https://mask-redis.readthedocs.io/en/latest
* Release: https://github.com/Eastwu5788/Mask-Redis/releases
* Code: https://github.com/Eastwu5788/Mask-Redis
* Issue tracker: https://github.com/Eastwu5788/Mask-Redis/issues
* Test status: https://coveralls.io/github/Eastwu5788/Mask-Redis
