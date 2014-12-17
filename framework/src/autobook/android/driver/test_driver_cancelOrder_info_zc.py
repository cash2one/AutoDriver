# coding=utf-8
__author__ = 'zhangchun'

import unittest
from framework.core import idriver_android
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_history_order(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity

        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)

        current_activity = self.driver.current_activity

        self.driver.find_id('personal_list_text').click()
        self.driver.wait_switch(current_activity)
        self.driver.find_id('rb_cancel').click()

        time.sleep(3)

        text=self.driver.find_id('order_number_text').text
        order_no=text.split(':')[1].strip()
        #获取列表第一个订单的订单号

        order_time=self.driver.find_id('order_time_text').text
        #获取列表第一个订单的时间

        order_info=self.driver.sql('SELECT insert_time FROM t_order_info a, t_order_history b WHERE a.id = b.order_info_id and a.order_no='+order_no)
        #获取数据库中该订单的时间

        self.assertTrue(order_time==unicode(order_info[0]))


