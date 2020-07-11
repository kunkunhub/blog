# 后端程序
from flask import Flask, escape, url_for
from flask import render_template as rp
app = Flask(__name__)


@app.route('/test')
def testindex():
    page = [                                        # 主页下网页链接
    {"url": url_for("hello"), "name": "Hello World"},
    {"url": url_for("move"), "name": "CSS移动"},
    {"url": url_for("js1"), "name": "JavaScript警告框"},
    {"url": url_for("js2"), "name": "JavaScript验证输入"},
    {"url": url_for("ionic"), "name": "加载图标"}
]
    return rp("index.html", page=page)

@app.route('/test/move')
def move():
    return rp("/test/move.html")

@app.route('/test/hello')
def hello():
    return rp("/test/hello.html")

@app.route('/learn')
def learn():
    return rp("/learn/1.html")

@app.route('/test/js1.html')
def js1():
    return rp("/test/js1.html")

@app.route('/test/js2')
def js2():
    return rp("/test/js2.html")

@app.route('/test/ionic')
def ionic():
    return rp("/test/ionic.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", threaded=True) #多线程