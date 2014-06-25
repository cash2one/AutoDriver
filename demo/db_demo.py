__author__ = 'Administrator'
# coding=utf-8

import os
from util import db
from util import fileUtil
import time

def main():
    # dbm = db.DBManager()
    # data = [('few', u'登陆火星计划不靠谱'),
    #          ('ad', u'如何系统性地保障软件的性能'),
    #          ('eae', u'数据库表测试')]
    #
    # sql = "INSERT INTO module values (NULL , ?, ?)"
    # dbm.insert_values(sql,data)
    # dbm.close_db()
    print time.ctime()

    #print fileUtil.filePath(__file__,True)


if __name__ =='__main__':
    main()