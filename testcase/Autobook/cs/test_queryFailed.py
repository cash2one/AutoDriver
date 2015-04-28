# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    查询失败
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def initInputValue(self,order_No,customer_Info,driver_Info):
        #订单号
        self.driver.find_id('orderNo').click()
        self.driver.find_id('orderNo').send_keys(order_No)
        #客户姓名/手机号码
        self.driver.find_id('customerInfo').click()
        self.driver.find_id('customerInfo').send_keys(customer_Info)
        #司机名称/司机工号
        self.driver.find_id('driverInfo').click()
        self.driver.find_id('driverInfo').send_keys(driver_Info)
        #点击查询按钮
        self.driver.find_id('query').click()


    def test_query1(self):
        '''
        #两个条件，输入不存在的手机号
        :return:
        '''
        self.initInputValue('14120417341988','13636460000','')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,u'提示信息不正确或不存在')


    def test_query2(self):
        '''
        #三个条件，输入不存在的司机工号
        :return:
        '''
        self.initInputValue('14120509209808','18502112941','sj_123')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,u'提示信息不正确或不存在')


    def test_query3(self):
        '''
        #一个条，件输入不存在的订单号
        :return:
        '''
        self.initInputValue('12314562','','')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,u'提示信息不正确或不存在')


    def test_query4(self):
        '''
         #一个条件，输入不存在客户手机号
        :return:
        '''
        self.initInputValue('','00010112','')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,u'提示信息不正确或不存在')


    def test_query5(self):
        '''
        #一个条件，输入不存在的客户名称
        :return:
        '''
        self.initInputValue('',u'王小二','')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,'false')

    #一个条件，输入不存在的客户名称
    # def test_query6(self):
    #     self.initInputValue('',u'王小二','')
    #     txt = self.driver.find_class('norecords').text
    #     print txt
    #     self.assertTrue(u'没有符合条件的数据...' in txt ,'false')


    def test_query7(self):
        '''
        #一个条件，输入不存在的司机工号
        :return:
        '''
        self.initInputValue('','','sj_123')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,u'提示信息不正确或不存在')


    def test_query8(self):
        '''
        #一个条件，输入不存在的司机名称
        :return:
        '''
        self.initInputValue('','',u'张张张')
        txt = self.driver.find_class('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,u'提示信息不正确或不存在')

