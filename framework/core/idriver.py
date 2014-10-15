# coding=utf-8
__author__ = 'Administrator'


from framework.core import the
from framework.util import mysql

def changeWork(isWorking):
    myself = the.android
    if the.i_driver['status'] != isWorking:
        myself.find_element_by_id('cn.com.pathbook.idriver.driver:id/tb_work_state').click()
        the.i_driver['status'] = isWorking

def find_data(table,field,value):
    '''
    idriver.find_data('t_driver','id','40')
    :param table:
    :param field:
    :param value:
    :return:
    '''
    dbm = mysql.DBManager('192.168.2.4','root','root','autobook')
    cu = dbm.get_cursor()
    cu.execute('select * from %s where %s=%s' %(table,field,value))
    r = cu.fetchall()
    cu.close()
    dbm.close_db()
    return r[0]