# 后端程序
from flask import Flask, escape, url_for
from flask import render_template as rp
app = Flask(__name__)

@app.route('/')
def hello():
    return rp("index.html")
    # 就可以显示index.html里的内容了！

@app.route('/move')
def move():
    return rp("/test/move.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", threaded=True) #多线程