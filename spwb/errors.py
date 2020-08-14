from spwb import app
from flask import abort, render_template

# 玩笑..
@app.route('/brew/coffee')
def brew_coffee():
    abort(418)

# 定义404页面视图函数
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('/err/404.html'), 404  # 返回模板和状态码

