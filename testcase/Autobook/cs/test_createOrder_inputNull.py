# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    创建订单的输入框为空
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_input_customerName(self):
        time.sleep(2)
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
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)

        #创建订单按钮
        self.driver.find_element_by_id('create_order_btn').click()
        #获取客户姓名为空提示信息并比较
        name=self.driver.find_element_by_id('customerCall_tip').text
        print name
        self.assertTrue(u'客户称呼不能为空.' in name,'客户姓名为空提示信息不正确或可以为空')

        #获取手机号为空提示信息并比较
        phone=self.driver.find_element_by_id('phone_tip').text
        print phone
        self.assertTrue(u'手机号码不能为空.' in phone,'手机号码为空提示信息不正确或可以为空')

        #获取客户位置为空提示信息并比较
        position=self.driver.find_element_by_id('position_tip').text
        print position
        self.assertTrue(u'客户位置不能为空.' in position,'客户位置为空提示信息部正确或可以为空')

        #获取司机为空提示信息并比较
        driverNam=self.driver.find_element_by_id('driverName_tip').text
        print driverNam
        self.assertTrue(u'请选择司机.' in driverNam,'没有选择司机，没有提示信息或可以不选择司机')
