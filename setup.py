# sys
from setuptools import setup


setup(
    name="mask-redis",
    install_requires=[
        "mask>=1.0.0a1",
        "redis>=3.5.3",
    ]
)
