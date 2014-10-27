# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import device,idriver
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_month_earning(self):
        idriver.changeWork(True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('rb_order').click()
        sum_earning=self.driver.find_id('he_sum').text
        self.driver.find_id('about_function').click()
        self.driver.wait_switch(current_activity)
        earnings=0.00
        for i in range(0,3) :

            text_earning=self.driver.find_ids('historyincome_income')[i].text
            earning=float(text_earning[1:])
            earnings+=earning
        self.assertTrue(unicode(earnings) in sum_earning)
