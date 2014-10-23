# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        #idriver.start_customer(self.driver)

    def tearDown(self):
        #返回首页
        #self.driver.switch_to_home()
        pass

    def test_my_info(self):
        #self.driver.find_id('rb_order').click()
        #time.sleep(1)

        print self.driver.find_id('tv_title_text').text


        time.sleep(1)

