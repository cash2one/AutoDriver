# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
import unittest
from framework.core import testcase
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_this_month_earning(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity
        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)

        current_activity = self.driver.current_activity
        self.driver.find_element_by_name(u'历史订单').click()
        self.driver.wait_switch(current_activity)

        text=self.driver.find_id('order_number_text').text
        order_no=text.split(':')[1].strip()
        #获取列表第一个订单的订单号

        amount_text=self.driver.find_id('order_amount_text').text
        amount=amount_text.split(':')[1].strip()
        order_amount=filter(str.isdigit,str(amount[:-1]))
        #获取列表第一个订单的合计费用

        order_time=self.driver.find_id('order_time_text').text
        #获取列表第一个订单的时间

        order_info=self.driver.sql('SELECT amount,insert_time FROM t_order_info a, t_order_history b WHERE a.id = b.order_info_id and a.order_no='+order_no)
        #获取数据库中该订单的合计费用及时间

        self.assertTrue(order_amount==str(order_info[0]))
        self.assertTrue(order_time==unicode(order_info[1]))
