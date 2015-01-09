__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
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
    def test_seeFlow(self):

        self.driver.find_ajax_id('communicationRecord')
        # table=self.driver.find_element_by_id('list')
        # trs=table.find_elements_by_tag_name('tr')
        # for i in range(1,len(trs)-1):
        #    orders= trs[i].find_elements_by_tag_name('td').text
        #    print orders
            #点击第一个通讯记录
           # if orders.get_attribute('text')==u'通讯记录':
        #点击第一个通讯记录
        self.driver.find_element_by_id('communicationRecord').click()
        time.sleep(2)



    #关闭通讯记录
    def test_seeFlow_close(self):

        self.driver.find_ajax_id('orderFlow')
        self.driver.find_element_by_id('communicationRecord').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('xubox_setwin').click()