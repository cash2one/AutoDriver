# coding=utf-8

"""
SQLite 操作类
"""

import sqlite3
import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class DBManager():

    def __init__(self,db_path):
        #sqlite3.connect(fp,check_same_thread = False)
        self.conn = sqlite3.connect(db_path)
        self.db_path = db_path

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
            cu.close()
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def create_table(self, sql):
        if sql is not None and sql != '':
            cu = self.get_cursor()
            cu.execute(sql)
            self.conn.commit()
            #print('创建数据库表成功!')
            cu.close()
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

    def insert_value(self, sql, data):
        '''插入数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()

                cu.execute(sql, data)
                self.conn.commit()

                row_id = cu.lastrowid

                self.close_all(cu)
                return row_id
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def insert_values(self, sql, data):
        '''插入数据'''
        row_ids = []
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    cu.execute(sql, d)
                    self.conn.commit()
                    row_ids.append(cu.lastrowid)

                self.close_all(cu)
                return row_ids
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    # def insert_Product_type(self,xls_path,xls_cfg):
    #     file_list = os.listdir(xls_path)
    #     re_f=re.compile(".xls$", re.IGNORECASE)
    #     files = filter(re_f.search, file_list)
    #
    #     #types=['web','android','ios','interface','windwosphone']
    #
    #     cfg = fs.readConfigs(xls_cfg,'product_type')
    #     data=[]
    #     for f in files:
    #         filename = os.path.basename(f).split('.xls')[0]
    #         if filename in cfg.keys():
    #             if cfg[filename] =='web':
    #                 data.append((filename,'gwe',1,0,0,0,0,1))
    #             elif cfg[filename] =='android':
    #                 data.append((filename,'wg',0,1,0,0,0,1))
    #             elif cfg[filename] =='ios':
    #                 data.append((filename,'gwe',0,0,1,0,0,1))
    #             elif cfg[filename] =='interface':
    #                 data.append((filename,'gwe',0,0,0,1,0,1))
    #             else:
    #                 data.append((filename,'gwee',0,0,0,0,1,1))
    #
    #     cu = self.get_cursor()
    #
    #     sql_product = 'INSERT INTO Product values (NULL,?,?,?,?,?,?,?,?)'
    #     sql_type = 'INSERT INTO ProductType values (NULL,?,?,?,?,?,?,?,?,?)'
    #
    #     for d in data:
    #         cu.execute(sql_product, d)
    #         lastid = cu.lastrowid
    #         self.conn.commit()
    #
    #         type_data=('gww',1,'','','','','','',lastid)
    #         cu.execute(sql_type, type_data)
    #         self.conn.commit()
    #
    #     cu.close()

    def fetchall(self, sql):
        '''查询所有数据'''
        if sql is not None and sql != '':
            cu = self.get_cursor()
            cu.execute(sql)
            r = cu.fetchall()
            cu.close()
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
                cu.close()
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
