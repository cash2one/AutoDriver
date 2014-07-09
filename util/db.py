# coding=utf-8

"""
SQLite 操作类
"""

import sqlite3
import os

class DBManager():

    def __init__(self):
        p=os.path.dirname(os.path.abspath(__file__))
        self.dbPath=os.path.dirname(p)+os.sep+'config'+os.sep+'autotest.db'
        self.conn = sqlite3.connect(self.dbPath)

    def get_cursor(self):
        if self.conn is not None:
            return self.conn.cursor()
        else:
            return self.conn.cursor()

    def drop_table(self, table):
        sql = 'DROP TABLE IF EXISTS ' + table
        if table is not None and table != '':
            cu = self.get_cursor()
            cu.execute(sql)
            self.conn.commit()
            print('删除数据库表[{}]成功!'.format(table))
            self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def create_table(self, sql):
        if sql is not None and sql != '':
            cu = self.get_cursor()
            cu.execute(sql)
            self.conn.commit()
            print('创建数据库表[student]成功!')
            self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def close_all(self, cu):
        '''关闭数据库游标对象和数据库连接对象'''
        try:
            if cu is not None:
                cu.close()
        finally:
            if cu is not None:
                cu.close()

    def close_db(self):
        self.conn.close()

    def insert_values(self, sql, data):
        '''插入数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    cu.execute(sql, d)
                    self.conn.commit()
                self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self, sql):
        '''查询所有数据'''
        if sql is not None and sql != '':
            cu = self.get_cursor()
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                return r
                # for e in range(len(r)):
                #     print(r[e])
        else:
            return None

    def fetchone(self, sql, data):
        '''查询一条数据'''
        if sql is not None and sql != '':
            if data is not None:
                #Do this instead
                d = (data,)
                cu = self.get_cursor()
                cu.execute(sql, d)
                r = cu.fetchall()
                if len(r) > 0:
                    for e in range(len(r)):
                        print(r[e])
            else:
                print('the [{}] equal None!'.format(data))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def update(self, sql, data):
        '''更新数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    cu.execute(sql, d)
                    self.conn.commit()
                self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def delete(self, sql, data):
        '''删除数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    cu.execute(sql, d)
                    self.conn.commit()
                self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))
