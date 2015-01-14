# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

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
    #押金付款,各项为空时提示的红色字体。
    def test_None_tips(self):

        self.driver.find_element_by_id('trade_pledgepay').click()
        self.driver.find_element_by_id('btn_pay').click()#点击充值
        time.sleep(3)
        #对比界面红色字体提示语。。
        companyAccount_tip_text = self.driver.find_element_by_id('companyAccountId_tip').text
        driver_tip_text = self.driver.find_element_by_id('driver_tip').text
        amount_tip_text = self.driver.find_element_by_id('amount_tip').text

        print companyAccount_tip_text,driver_tip_text,amount_tip_text
        self.assertTrue(u'请选择充入账户.' in companyAccount_tip_text,'msg')
        self.assertTrue(u'充值司机不能为空.' in driver_tip_text,'msg')
        self.assertTrue(u'充值金额（元）不能为空.' in amount_tip_text,'msg')
        time.sleep(3)


if __name__ =='__main__':
    unittest.main()


