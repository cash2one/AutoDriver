# coding=utf-8
__author__ = 'Administrator'


from framework.core import the

def changeWork(isWorking):
    myself = the.android
    if the.i_driver['status'] != isWorking:
        myself.find_element_by_id('cn.com.pathbook.idriver.driver:id/tb_work_state').click()
        the.i_driver['status'] = isWorking