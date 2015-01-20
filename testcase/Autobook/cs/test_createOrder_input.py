# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    验证创建订单的输入框
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

     #点击创建订单跳转到创建订单界面
    def test_input_customerName(self):
        self.driver.find_ajax_id('main_menu')
        self.driver.find_element_by_id('main_menu').click()
        # print menu
        #
        # for i in range(0,len(menu)-1):
        #     if menu[i]==u'订单管理':
        self.driver.find_element_by_link_text('订单管理').click()
        time.sleep(3)
        self.driver.find_element_by_link_text('创建订单').click()
        time.sleep(5)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url)
        finally:
            pass
        #time.sleep(3)
        #客户姓名输入非法字符
        self.driver.find_element_by_id('customerCall').send_keys(u'#@&%')
        #创建订单按钮
        self.driver.find_element_by_id('create_order_btn').click()
        text=self.driver.find_element_by_id('customerCall_tip').text
        self.assertTrue(u'客户称呼含有非法字符.' in text,'msg')




    def test_input_customerphone(self):
        self.driver.find_ajax_id('main_menu')
        self.driver.find_element_by_id('main_menu').click()
        # print menu
        #
        # for i in range(0,len(menu)-1):
        #     if menu[i]==u'订单管理':
        self.driver.find_element_by_link_text('订单管理').click()
        time.sleep(3)
        self.driver.find_element_by_link_text('创建订单').click()
        time.sleep(5)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url)
        finally:
            pass
        #time.sleep(3)
        #输入的手机号少于11位
        self.driver.find_element_by_id('customerCall').send_keys('wss')
        self.driver.find_element_by_id('phone').send_keys('1359807')
        #创建订单按钮
        self.driver.find_element_by_id('create_order_btn').click()
        text=self.driver.find_element_by_id('phone_tip').text
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.' in text,'msg')


        #输入的手机号大于于11位,系统限制输入
    # def test_input_customerphone1(self):
    #     self.driver.find_ajax_id('main_menu')
    #     self.driver.find_element_by_id('main_menu').click()
    #     # print menu
    #     #
    #     # for i in range(0,len(menu)-1):
    #     #     if menu[i]==u'订单管理':
    #     self.driver.find_element_by_link_text('订单管理').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_link_text('创建订单').click()
    #     time.sleep(5)
    #     try:
    #         self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url)
    #     finally:
    #         pass
    #     #time.sleep(3)
    #     #输入的手机号大于于11位
    #     self.driver.find_element_by_id('customerCall').send_keys('wss')
    #     self.driver.find_element_by_id('phone').send_keys('1363646871356')
    #     #创建订单按钮
    #     self.driver.find_element_by_id('create_order_btn').click()
    #     text=self.driver.find_element_by_id('phone_tip').text
    #     self.assertTrue(u'手机号码输入错误,请输入11位手机号码.' in text,'msg')



        #客户手机号输入特殊字符
    def test_input_customerphone2(self):
        self.driver.find_ajax_id('main_menu')
        self.driver.find_element_by_id('main_menu').click()
        # print menu
        #
        # for i in range(0,len(menu)-1):
        #     if menu[i]==u'订单管理':
        self.driver.find_element_by_link_text('订单管理').click()
        time.sleep(3)
        self.driver.find_element_by_link_text('创建订单').click()
        time.sleep(5)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url)
        finally:
            pass
        #time.sleep(3)
        self.driver.find_element_by_id('customerCall').send_keys('wss')
        #输入的手机号为特殊字符
        self.driver.find_element_by_id('phone').send_keys(u'￥%￥#')
        #创建订单按钮
        self.driver.find_element_by_id('create_order_btn').click()
        text=self.driver.find_element_by_id('phone_tip').text
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.' in text,'msg')
