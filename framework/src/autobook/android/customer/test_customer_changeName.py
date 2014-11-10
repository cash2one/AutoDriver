# coding=utf-8

__author__ = 'wangsahnshan'

import time
import unittest
from framework.core import device,idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.customer')
        idriver.login_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击用户中心
       self.driver.find_id('btn_personalcenter').click()
       #点击历史订单
       self.driver.find_ids('personal_name')[1].click()
       #点击待评价的订单
       self.driver.swipe('lv_finish','order_Eval','待评价').clidk()
