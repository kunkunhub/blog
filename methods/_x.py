import db
import os
import sys
from pprint import pprint as pt

def hlp():
    h = """\
这是一个用于操作这个项目的轻量级终端，方便快捷。
以下是常用命令：
help            --显示帮助信息
exit            --退出
cls             --清屏

new-article     --新建文章
del-article     --删除文章          --开发中
list-article    --查看文章列表      
show-article    --查看文章(html)    --开发中

python          --进入python终端
cmd             --进入cmd终端
sql             --进入sqlite3终端
run             --运行服务
高级（谨慎使用）：
set-id          --设置id            --开发中
list-id         --查看已经使用的id   --开发中
create-table     --在数据库里创建表article       
drop-table      --删除表article     --开发中
"""
    print(h)

def new_article():
    print("新建文章")
    x = input("""\
[1]: 直接输入
[2]: 从文件导入
<其它输入>: 退出
请选择新建文章的方式(输入序号)：\
""")
    if x == "1":
        print('请输入文章内容, 输入"-*-end-*-"结束(文章为markdown格式)：\n')
        l = ""
        while(True):
            m = input()
            if m == "-*-end-*-":
                break
            l = f"{l}\n{m}"
    elif x == "2":
        print("请输入文件的相对路径或绝对路径并带上后缀名：")
        f = open(input(), "r")
        l = f.read()
    else:
        return
    t = input("文章标题：")
    x = input("确认提交？[y]|n: ")
    if x != "y" and x != "":
        return
    db.new_article(t, l)

    print("提交成功")

def create_table():
    try:
        db.cur.execute("""\
CREATE TABLE article(
   id integer PRIMARY KEY autoincrement,
   title          varchar(100)    NOT NULL,
   content        longtext     NOT NULL
);
""")
    except Exception as e:
        print("创建表出错:", e)

def list_article():
    pt(db.article_list())

u = {
    "help": hlp,
    "": lambda : None,
    "new-article": new_article,
    "create-table": create_table,
    "python": lambda : os.system(f"{sys.executable}"),
    "cmd": lambda : os.system("cmd"),
    "sql": lambda : os.system(f"sqlite3 {os.path.dirname(__file__)}\\db.sqlite3"),
    "list-article": list_article,
    "run": lambda : os.system(
    f'cd /d {os.path.dirname(__file__)} && cd .. && {sys.executable} server.py'),
    "cls": lambda : os.system("cls")
}
print('欢迎进入项目操作终端！\n键入"exit"退出，键入"help"获取更多消息')
while(True):
    cmd = input("shell> ")
    if cmd == "exit":
        print("bye")
        sys.exit(0)
    try:
        u[cmd]()
    except KeyError:
        print(f"未找到命令：{cmd}, 输入help查看帮助信息。")
    except KeyboardInterrupt:
        print("用户退出")
    except Exception as e:
        print(f"捕获异常：{e}")
        if input("是否忽略？[y]|n : ") != "n":
            pass
        else:
            raise
print("bye")


