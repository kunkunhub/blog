
from sqlite3 import connect, IntegrityError
import markdown
import pickle
import os
conn = connect(f"{os.path.dirname(__file__)}\\db.sqlite3")
cur = conn.cursor()


f = open(f"{os.path.dirname(__file__)}\\id.dat", "rb+")

id = pickle.load(f) 

def new_article(title: str, markd: str)->int:
    global id
    html = markdown.markdown(markd, output_format="html5")
    try:
        cur.execute("insert into `article` (title, content) values (?, ?);", (title, html))
    except IntegrityError:
        id += 1
        cur.execute("insert into `article` (title, content) values (?, ?);", (title, html))
    conn.commit()
    id += 1
    pickle.dump(id, f)
    f.flush()
    return id-1

def get_article(id):
    cur.execute("SELECT title, content FROM `article` WHERE id=?;", (id,))    
    #sqlite3.OperationalError: no such table: article
    return cur.fetchall()[0]

def article_list():
    cur.execute("SELECT id, title FROM `article`")
    return cur.fetchall()[0]


def stop():
    conn.commit()
    cur.close()
    conn.close()
    pickle.dump(id, f)
    f.flush()
    f.close()


