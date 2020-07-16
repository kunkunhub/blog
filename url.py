#!/usr/bin/env Python
# coding=utf-8
"""
网站页面的url对应的请求类
"""
from handlers.index import IndexHandler


url = [
    (r'/', IndexHandler),   #网站目录
]