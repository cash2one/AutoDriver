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
    def test_input_customerName(self):
        '''
        客户姓名输入非法字符
        :return:
        '''
        time.sleep(1)
        self.driver.find_ajax_id('main_menu')
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('创建订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)
        #客户姓名输入非法字符
        self.driver.find_id('customerCall').send_keys(u'#@&%')
        #创建订单按钮
        self.driver.find_id('create_order_btn').click()
        text=self.driver.find_id('customerCall_tip').text
        self.assertTrue(u'客户称呼含有非法字符.' in text,'msg')




    def test_input_customerphone(self):
        '''
        #输入的手机号小于11位,弹出提示信息
        :return:
        '''
        self.driver.find_ajax_id('main_menu')
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('创建订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)
        #输入的手机号少于11位
        self.driver.find_id('customerCall').send_keys('wss')
        self.driver.find_id('phone').send_keys('1359807')
        #创建订单按钮
        self.driver.find_id('create_order_btn').click()
        text=self.driver.find_id('phone_tip').text
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.' in text,u'手机号输入少于11位没有提示信息或提示信息不正确')



    # def test_input_customerphone1(self):
    #     '''
    #     #输入的手机号大于于11位,系统限制输入
    #     :return:
    #     '''
    #     self.driver.find_ajax_id('main_menu')
    #     self.driver.find_id('main_menu').click()
    #     # print menu
    #     #
    #     # for i in range(0,len(menu)-1):
    #     #     if menu[i]==u'订单管理':
    #     self.driver.find_link('订单管理').click()
    #     time.sleep(3)
    #     self.driver.find_link('创建订单').click()
    #     time.sleep(5)
    #     try:
    #         self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
    #     finally:
    #         pass
    #     #time.sleep(3)
    #     #输入的手机号大于于11位
    #     self.driver.find_id('customerCall').send_keys('wss')
    #     phone=self.driver.find_id('phone')
    #     phone.send_keys('1363646847523')
    #     #创建订单按钮
    #     self.driver.find_id('create_order_btn').click()
    #     text=self.driver.find_id('phone_tip').text
    #     self.assertTrue(u'手机号码输入错误,请输入11位手机号码.' in text,u'手机号输入超过11位没有提示信息或提示信息不正确')




    def test_input_customerphone2(self):
        '''
        #客户手机号输入特殊字符
        :return:
        '''
        self.driver.find_ajax_id('main_menu')
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('创建订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)
        self.driver.find_id('customerCall').send_keys('wss')
        #输入的手机号为特殊字符
        self.driver.find_id('phone').send_keys(u'￥%￥#')
        #创建订单按钮
        self.driver.find_id('create_order_btn').click()
        text=self.driver.find_id('phone_tip').text
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.' in text,u'手机号输入特殊字符，提示信息不正确或没有提示信息')
