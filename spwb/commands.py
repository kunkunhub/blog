from spwb import app, db
from spwb.models import Article
from markdown import markdown
import click

@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

@app.cli.command()
def newartc():
    print('请输入文章标题：', end='')
    t = input()
    print('请输入文章正文，输入"---end---"结束输入')
    md = ""
    a = ''
    while not (a == '---end---'):
        a = input()
        md = md + "\n" + a
    print('正在转换为html')
    html = markdown(md)
    print("正在写入数据库")
    newartc = Article(title=t, content=html)
    db.session.add(newartc)
    db.session.commit()
    print("完成")

