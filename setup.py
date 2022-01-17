# sys
import os
from codecs import open
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


requires = [
    "mask>=1.0.0",
    "redis>=4.1.0"
]


about = {}
with open(os.path.join(here, 'mask_redis', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)


readme = None
if os.path.exists('README.md'):
    with open('README.md', 'rb') as f:
        readme = f.read().decode("utf-8")


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*", "docker", "docs"]),
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
