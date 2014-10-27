# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_my_info(self):
        idriver.changeWork(self.driver,True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('iv_head').click()

        self.driver.wait_switch(current_activity)

        title_text = self.driver.find_id('tv_title_text').text

        print self.driver.sql('select name from t_driver where id=40')
        self.assertTrue(u'个人中心' in title_text,'no')

        idriver.request_order(True)

