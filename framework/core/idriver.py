# coding=utf-8
__author__ = 'Administrator'


from framework.core import the
from framework.util import mysql


def changeWork(isWorking):
    myself = the.android
    if the.i_driver['status'] != isWorking:
        myself.find_element_by_id('cn.com.pathbook.idriver.driver:id/tb_work_state').click()
        the.i_driver['status'] = isWorking

def find_data(sql):
    '''
    查询mysql数据
    :param sql:
    :return:
    '''
    db_conf = the.settings['database']
    my_dbm = mysql.DBManager(db_conf['host'],db_conf['user'],db_conf['pwd'],db_conf['db'])

    cu = my_dbm.get_cursor()
    cu.execute(sql)
    r = cu.fetchone()
    cu.close()
    my_dbm.close_db()
    return r