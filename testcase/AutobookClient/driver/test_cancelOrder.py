# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import datetime
from framework.core import testcase
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
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
        self.driver.find_element_by_name(u'历史订单').click()
        self.driver.wait_switch(current_activity)
        self.driver.find_element_by_name(u'已取消').click()
        self.driver.wait_find_id("rb_cancel")
        orders1_no=()
        for i in range(0,5):
            text=self.driver.find_ids('order_number_text')[i].text
            order_no=text.split(':')[1].strip()
            orders1_no+=((order_no,),)
        #获取当前页面上的所有订单号


        orders2_no=self.driver.sql('SELECT a.order_no FROM t_order_info a, t_driver b WHERE a.driver_id = b.id and b.no =%s ORDER BY a.create_time desc' % self.driver.no,0,1)
        #在数据库中关联查询该司机的所有订单

        #print(type(orders1_no[1]),type(orders2_no[1]))
        print orders1_no
        print orders2_no

        isExist = True
        for no in orders1_no:
            if no not in orders2_no:
                isExist = False
                break

        self.assertTrue(isExist,'false')

