import db
import os
import sys
from pprint import pprint as pt
sys.path.append("..\\")
import server
import threading as th

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
show-article    --查看文章(html) 

install         --安装依赖项，初始化项目
installpkg      --快捷安装某个包
python          --进入python终端
ipython         --进入ipython终端
cmd             --进入cmd终端
sql             --进入sqlite3终端
run             --运行服务
高级（谨慎使用）：
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
        print('请输入文章内容, 输入"---end---"结束(文章为markdown格式)：\n')
        l = ""
        while(True):
            m = input()
            if m == "---end---":
                break
            l = f"{l}\n{m}"
    elif x == "2":
        print("请输入文件的相对路径或绝对路径并带上后缀名：")
        f = open(input(), "r", encoding="utf-8")
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

running = False

def run():
    global running
    if not running:
        print("启动服务器...")
        try:
            running = True
            server.main()
        except KeyboardInterrupt:
            print("程序结束")
        except Exception as e:
            print(f"运行服务时出错：{e}")
        running = False
    else:
        print("服务器已经在运行了！输入stop停止。")
    
def show_article():
    article = db.get_article(input('请输入文章的id: '))
    print(f"标题：{article[0]}")
    print("正文：")
    pt(article[1])

def install_pkg():
    os.system(f"""{sys.executable} -m pip install -i \
https://pypi.tuna.tsinghua.edu.cn/simple {input("要安装的包（空格分隔多个包名）：")}""")

def install():
    print("初始化")
    pkglist = [
        "tornado",
        "markdown"
    ]
    for i in pkglist:
        os.system(f"""{sys.executable} -m pip install -i \
https://pypi.tuna.tsinghua.edu.cn/simple {i}""")
    create_table()


path = os.path.dirname(__file__)
u = {
    "help": hlp,
    "": lambda : None,
    "new-article": new_article,
    "create-table": create_table,
    "python": lambda : os.system(f"{sys.executable}"),
    "cmd": lambda : os.system("cmd"),
    "sql": lambda : os.system(f"sqlite3 {path}\\db.sqlite3"),
    "list-article": list_article,
    "run": run,
    "show-article": show_article,
    "ipython": lambda : os.system("ipython"),
    "install-pkg": install_pkg,
    "install": install,

}
def main():
    print('欢迎进入项目操作终端！\n键入"exit"退出，键入"help"获取更多信息')
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

if __name__ == "__main__":
    main()
