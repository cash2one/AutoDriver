# coding=utf-8
__author__ = 'zhangchun'

import datetime
from framework.core import device,idriver
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_history_order(self):
        idriver.changeWork(self.driver,True)



