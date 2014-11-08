# coding=utf-8
__author__ = 'zhangchun'

import time
from framework.core import idriver_android
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.driver()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_time_control(self):
        self.driver.change_status(True)

        current_activity = self.driver.current_activity
        #获取待补订单列表中订单的信息
        self.driver.find_element_by_id(self.driver.pkg + 'iv_detail').click()
        self.driver.wait_switch(current_activity)

        ctime=self.driver.find_element_by_id(self.driver.pkg + 'ro_ctime').text

        self.driver.find_element_by_id(self.driver.pkg + 'ro_endtime').click()

        self.driver.switch_to_alert()
        self.driver.find_id('btn_ok').click()
        time.sleep(2)
        time=self.driver.find_element_by_id(self.driver.pkg + 'ro_endtime').text

        self.assertTrue(ctime[:-3]==time)

        print ctime[:-3],time