#!/usr/bin/env Python
# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options
from application import application
define("port", default=8000, help="run on the given port", type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print(f"服务运行在：http://127.0.0.1:{options.port}")
    print(f"Ctrl-C结束程序(如果Ctrl-C没反应再去访问一下127.0.0.1:{options.port}就行)")

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("结束程序")