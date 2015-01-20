# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_month_earning(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        # 获取待补订单列表中订单的信息
        self.driver.find_id('iv_detail').click()
        self.driver.wait_switch(current_activity)
        self.driver.find_id('confirm_repairorder').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'结束时间不能为空' in txt)