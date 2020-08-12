from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click
app = Flask(__name__)


# ------ 数据库配置 ------ #

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(
    app.root_path, 'data.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)


# ------ 数据库操作 ------ #

@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

@app.route('/')
def index():        #主页
    return render_template("index.html")

@app.route('/about')
def about():        #关于页面
    return render_template("about.html")