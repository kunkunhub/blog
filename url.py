#!/usr/bin/env Python
# coding=utf-8
"""
网站页面的url对应的请求类
"""
from handlers.index import IndexHandler
from handlers.article import ArticleHandler
from handlers.about import AboutHandler

url = [
    (r'/', IndexHandler),   #网站目录
    (r'/article/([0-9]+)', ArticleHandler),
    (r'/about', AboutHandler)
]