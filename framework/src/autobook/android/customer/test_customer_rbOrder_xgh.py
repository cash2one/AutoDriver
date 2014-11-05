# coding=utf-8
__author__ = 'xuguanghua'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.customer')
        idriver.login_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_rb_Order(self):
        current_activity = self.driver.current_activity
        #点击一键下单，进入一键下单界面
        self.driver.find_id('rb_order').click()
        #切换2人，3人，4人，1人按钮
        self.driver.find_id('person_two').click()
        self.driver.find_id('person_three').click()
        self.driver.find_id('person_four').click()
        self.driver.find_id('person_one').click()
        #点击立即下单
        self.driver.find_id('bt_order').click()
        self.driver.wait_switch(current_activity)
        self.driver.switch_to_alert()







