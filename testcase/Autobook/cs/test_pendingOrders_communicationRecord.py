# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

#待处理订单页面：查看通讯记录、关闭通讯记录



import time
import unittest
from framework.core import idriver_web

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #查看通讯记录
    def test_communicationRecord(self):

        self.driver.find_ajax_id('communicationRecord')
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #取第一行第一列的订单号
        for i in range(1,len(trs)-1):
         CR=trs[i].find_elements_by_tag_name('td')[10]
         if CR.find_elements_by_link_text('通讯记录'):
              self.driver.find_element_by_id('communicationRecord').click()

        time.sleep(2)



    #关闭通讯记录
    def test_close_communicationRecord(self):

        self.driver.find_ajax_id('orderFlow')
        self.driver.find_element_by_id('communicationRecord').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('xubox_setwin').click()