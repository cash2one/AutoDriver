# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_finish_Order(self):
        current_activity = self.driver.current_activity
        #点击用户中心图标，进入用户中心列表
        self.driver.find_id('btn_personalcenter').click()
        self.driver.wait_loading()

        #点击历史订单
        personal_names = self.driver.find_ids('personal_name')
        personal_names[1].click()
        self.driver.wait_loading()

        #获取已完成订单列表的订单号
        order_Nos = self.driver.find_id('order_no').text

        #获取已完成订单列表的订单金额
        order_amounts = self.driver.find_id('order_amount').text

        #获取已完成订单列表的订单完成时间
        order_dates = self.driver.find_id('order_date').text

        list_info = (order_amounts,order_dates)
        print list_info

        #拿列表最近一个订单号从数据库中取出该订单的金额和完成时间
        order_info = self.driver.sql('SELECT amount,insert_time FROM t_order_info a, t_order_history b WHERE a.id = b.order_info_id and a.order_no='+order_Nos,1)

        #长整形转换为整形hhh
        sql_info =self.driver.enum(int(order_info[0]),str(order_info[1]))

        print sql_info

        self.assertTrue((int(order_amounts))*100 == sql_info[0])




