#!/usr/bin/env Python
# coding=utf-8

from url import url     #������վĿ¼

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),   #����Ŀ¼
    static_path = os.path.join(os.path.dirname(__file__), "statics")
)

application = tornado.web.Application(
    handlers = url,
    **settings
)
