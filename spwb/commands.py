from spwb import app, db
from spwb.models import Article, Admin
from markdown import markdown
import click
from faker import Faker

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
    print('请输入对文章的描述：')
    d = input()
    print('请输入文章正文，输入"---end---"结束输入')
    md = ""
    a = ''
    while True:
        a = input()
        if a != "---end---":
            md = md + "\n" + a
        else:
            break
    print('正在转换为html')
    html = markdown(md)
    print("正在写入数据库")
    newartc = Article(title=t, content=html, describe=d)
    db.session.add(newartc)
    db.session.commit()
    print("完成")

@app.cli.command()
@click.option('--count', default=10000, help="创建虚拟文章，默认5000")
def forge(count):
    """创建虚拟文章"""
    fake = Faker()
    click.echo("工作中...")
    for i in range(count):
        artc = Article(
            title=fake.name(),
            content=fake.text(1000),
            describe=fake.sentence()
        )
        db.session.add(artc)
        if i%100 == 0:
            print(i/count*100, end='\r')
            db.session.commit()
    db.session.commit()
    click.echo("完成！")

@app.cli.command()
@click.option('--username', prompt=True, help="用户名")
@click.option('--password', prompt=True, help="密码")
def init(username, password):
    """
    初始化管理员，如果已经有管理员就覆盖。
    """
    click.echo("初始化数据库")
    db.create_all()

    admin = Admin.query.first()
    if admin:
        pass