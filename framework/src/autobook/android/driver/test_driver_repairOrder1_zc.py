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
        current_activity = self.driver.current_activity
        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)

        current_activity = self.driver.current_activity
        self.driver.find_element_by_name(u'历史订单').click()
        self.driver.wait_switch(current_activity)

        text1=self.driver.find_id('order_number_text').text
        order_no=text1.split(':')[1]
        #获取最近一个订单的订单号

        # text2=self.driver.find_id('order_amount_text').text
        # t=text2.split(':')[1]
        # order_amount=filter(str.isdigit,str(t[:-1]))
        # #获取最近一个订单的费用合计
        #
        # text3=self.driver.find_id('order_time_text').text
        # order_time=text3.split(':')[1]
        # #获取最近一个订单的时间
        #
        # text4=self.driver.find_id('completed_saddr').text
        # order_time=text3.split(':')[1]
        # #获取最近一个订单的时间


        orders_no=self.driver.sql('SELECT a.order_no FROM t_order_info a, t_driver b WHERE a.driver_id = b.id and b.no =140013',1)
        #self.assertTrue(order_no in orders_no)
        print(orders_no)