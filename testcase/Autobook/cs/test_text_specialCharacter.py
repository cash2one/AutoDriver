# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    文本框中输入特殊字符
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_order_query(self):
        '''
        #根据订单号查询
        :return:
        '''
        time.sleep(3)
        self.driver.find_id('orderNo').send_keys(u'@￥%…')
        time.sleep(1)
        self.driver.find_id('query').click()
        time.sleep(2)
        text=self.driver.find_class('norecords').text
        print text
        self.assertTrue(u'没有符合条件的数据...' in text,u'提示信息部正确或不存在')


    def test_customer_query(self):
        '''
        客户查询条件输入框输入特殊字符
        :return:
        '''
        self.driver.find_ajax_id('customerInfo')
        time.sleep(3)
        self.driver.find_id('customerInfo').send_keys(u'#￥%…')
        time.sleep(1)
        self.driver.find_id('query').click()
        time.sleep(2)
        text=self.driver.find_class('norecords').text
        print text
        self.assertTrue(u'没有符合条件的数据...' in text,u'提示信息部正确或不存在')


    def test_driver_query(self):
        '''
        司机查询条件输入框输入特殊字符
        :return:
        '''
        self.driver.find_ajax_id('driverInfo')
        time.sleep(3)
        self.driver.find_id('driverInfo').send_keys(u'%%…')
        time.sleep(1)
        self.driver.find_id('query').click()
        time.sleep(2)
        text=self.driver.find_class('norecords').text
        print text
        self.assertTrue(u'没有符合条件的数据...' in text,u'提示信息部正确或不存在')
