# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)
        self.pkg = self.driver.package

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()
        pass

    def test_my_info(self):
        idriver.changeWork(self.driver,True)

        # name_id = self.driver.wait_id_text('tv_customer_name',u'xu女士')
        #
        # print 'pass.....'
        print self.pkg
        txt = self.driver.find_id('ll_order_body').find_id('tv_order_id').text
        print txt

