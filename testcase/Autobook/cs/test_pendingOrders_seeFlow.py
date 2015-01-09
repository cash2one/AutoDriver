__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
#待处理订单页面：查看流程、关闭流程



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

    #查看订单流程
    def test_seeFlow(self):
        self.driver.find_ajax_id('orderFlow')
        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #点击第一行的“订单流程”
        trs[1].find_element_by_id('orderFlow').click()
        time.sleep(2)


    #关闭订单流程
    def test_seeFlow_close(self):
        self.driver.find_ajax_id('orderFlow')
        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #点击第一行的“订单流程”
        trs[1].find_element_by_id('orderFlow').click()
        # time.sleep(2)
        self.driver.find_element_by_class_name('xubox_setwin').click()