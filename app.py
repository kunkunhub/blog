import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler): # 继承
    def get(self):                              # 处理的请求方法
        msg = self.get_argument('msg', 'Hello, World!')   
        # 获取请求参数"msg"默认为"Hello"
        self.write(msg)   # 输出

if __name__ == "__main__":
    tornado.options.parse_command_line()    # 解析命令行
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)]) 
    # !handlers=[(r"<url>", <类>)]
    http_server = tornado.httpserver.HTTPServer(app) # !
    http_server.listen(options.port)    # !!
    print(f"服务器正在监听端口{options.port}")
    tornado.ioloop.IOLoop.instance().start() # 循环监听!!!
    