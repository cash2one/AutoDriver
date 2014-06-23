__author__ = 'Administrator'
# coding=utf-8

import os
import sqlite3

SHOW_SQL = True

def get_conn(path):
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print(u'硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        print(u'内存上面:[:memory:]')
        return sqlite3.connect(':memory:')

def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()

def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()

def create_table(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('创建数据库表[student]成功!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def update(conn, sql, data):
    '''更新数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def create_table_test():
    create_table_sql = "CREATE TABLE IF NOT EXISTS 'Plan'('id' INTEGER PRIMARY KEY AUTOINCREMENT,'planName' VARCHAR NOT NULL,'planType' INTEGER NOT NULL,'createWay' INTEGER NOT NULL,'planNumber' INTEGER NOT NULL,'exceptions' VARCHAR,'isFinish' INTEGER NOT NULL,'duration' FLOAT NOT NULL,'createTime' DATETIME,'updateTime' DATETIME)"
    create_table(get_conn(), create_table_sql)