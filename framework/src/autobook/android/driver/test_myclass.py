# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver.Application('driver')
        self.driver.login()
        self.android = self.driver.ium
        self.pkg = self.driver.package

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()
        pass

    def test_my_info(self):
        #idriver.changeWork(self.driver,True)

        # name_id = self.driver.wait_id_text('tv_customer_name',u'xu女士')
        #
        # print 'pass.....'
        # print self.pkg
        # self.driver.find_id('rb_benifit').click()
        # he_td = self.driver.wait_find_id('he_td')


        # #自动下单
        # order_owner = u'AutoZh'
        # self.driver.send_new_order(order_owner)
        # tv_customer_name = self.driver.wait_find_id_text('tv_customer_name',order_owner)
        #
        # print tv_customer_name.text
        print self.driver.enum('provinces',1)

        txt = self.android.find_element_by_id(self.pkg+'rl_title').find_element_by_id(self.pkg+'tv_title_text').text
        print txt


