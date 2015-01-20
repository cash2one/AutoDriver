# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
    #预付款充值,各项为空时提示的红色字体。
    def test_None_tips(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('btn_manul').click()#点击充值
        time.sleep(4)
        #对比界面红色字体提示语。。
        companyAccount_tip_text = self.driver.find_element_by_id('companyAccountId_tip').text
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        amount_tip_text = self.driver.find_element_by_id('amount_tip').text

        print companyAccount_tip_text,driver_tip_text,amount_tip_text
        self.assertTrue(u'请选择充入账户.' in companyAccount_tip_text,'msg')
        self.assertTrue(u'充值司机不能为空.' in driver_tip_text,'msg')
        self.assertTrue(u'充值金额（元）不能为空.' in amount_tip_text,'msg')
        time.sleep(3)

