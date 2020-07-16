#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tornado.web import RequestHandler
class IndexHandler(RequestHandler): # 继承
    def get(self):                              # 处理的请求方法
        msg = self.get_argument('msg', 'Hello, World!')   
        # 获取请求参数"msg"默认为"Hello"
        self.render("index.html")   # 输出
