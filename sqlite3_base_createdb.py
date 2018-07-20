### using SQLite
# ref : http://www.mwsoft.jp/programming/python/sqlite3.html
#       https://qiita.com/mas9612/items/a881e9f14d20ee1c0703
#       
# next: Flask - SQLAlchemy
#  http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
#  https://qiita.com/xecus/items/b437513cbb9f0e1aa87a
#  https://github.com/sagaragarwal94/python_rest_flask/blob/master/server.py
#
#  to setup vscode : disable pylint -> enable flake8
#
import sqlite3
from contextlib import closing


_db_name = 'sqlite3test.db'
_test_table = 'crudtest_tbl'

#conn = sqlite3.connect('sqlite3test.db')
with closing(sqlite3.connect(_db_name)) as conn:
    # create database
    cur = conn.cursor()
    
    sql_createdb = f'create table {_test_table} (id int, name varchar(64), age int, gender varchar(32))'

#    sql_dropdb = f'drop table {_test_table}'
#    cur.execute(sql_dropdb)

    cur.execute(sql_createdb)
    
    # insert
    sql_insert = f'insert into {_test_table} (id, name, age, gender) values (?,?,?,?)'
    user1 = [1, 'Ichiro', 22, 'male']
    cur.execute(sql_insert, user1)

    users = [
        (2, 'Shota', 54, 'male'),
        (3, 'Nana', 40, 'female'),
        (4, 'Tooru', 78, 'male'),
        (5, 'Saki', 31, 'female')
    ]

    cur.executemany(sql_insert, users)
    
    conn.commit()

    # Select
    sql_select = f'select * from {_test_table}'
    for row in cur.execute(sql_select):
        print(row)