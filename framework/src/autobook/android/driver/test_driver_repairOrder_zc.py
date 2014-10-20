# coding=utf-8
__author__ = 'zhangchun'

import time
from framework.core import extend,idriver
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = extend.Android('android.idriver.driver')
        self.driver.login()
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_month_earning(self):
        idriver.changeWork(True)
        current_activity = self.driver.current_activity()
        #获取待补订单列表中订单的信息
        self.driver.find_id('iv_detail').click()
        self.driver.switch_finish(current_activity)
        self.driver.find_id('confirm_repairorder').click()
        self.driver.switch_to_alert()
        txt=self.driver.find_id('tv_msg').text
        self.assertTrue(u'结束时间不得为空' in txt)