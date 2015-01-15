# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'



import time
import unittest
from framework.core import testcase
from selenium.common import exceptions

class TestCase(unittest.TestCase):
    '''
    文本框中输入特殊字符
    '''

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #根据订单号查询
    def test_order_query(self):

        time.sleep(3)
        self.driver.find_element_by_id('orderNo').send_keys(u'@￥%…')
        time.sleep(1)
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        text=self.driver.find_element_by_class_name('norecords').text
        print text
        self.assertTrue(u'没有符合条件的数据...' in text,'msg')


    def test_customer_query(self):
        self.driver.find_ajax_id('customerInfo')
        time.sleep(3)
        self.driver.find_element_by_id('customerInfo').send_keys(u'#￥%…')
        time.sleep(1)
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        text=self.driver.find_element_by_class_name('norecords').text
        print text
        self.assertTrue(u'没有符合条件的数据...' in text,'msg')


    def test_driver_query(self):
        self.driver.find_ajax_id('driverInfo')
        time.sleep(3)
        self.driver.find_element_by_id('driverInfo').send_keys(u'%%…')
        time.sleep(1)
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        text=self.driver.find_element_by_class_name('norecords').text
        print text
        self.assertTrue(u'没有符合条件的数据...' in text,'msg')