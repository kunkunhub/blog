#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tornado.web import RequestHandler
class IndexHandler(RequestHandler): # 继承
    def get(self):                              # 处理的请求方法
        self.render("index.html")   # 输出
