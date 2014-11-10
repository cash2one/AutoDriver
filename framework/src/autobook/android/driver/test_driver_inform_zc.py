# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import idriver_android
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.driver()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_this_month_earning(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity
        try:
            el=self.driver.find_id('tv_msg_count')
            if el.is_displayed():
                text1=el.text

                self.driver.find_id("iv_head").click()
                self.driver.wait_switch(current_activity)
                text2=self.driver.find_id("personal_msg_count").text
                self.driver.find_element_by_name(u"消息公告").click()
                red=self.driver.find_ids('bulletin_read')
                text3=len(red)
                self.assertTrue(text1==text2==unicode(text3))
            else:
                pass

        except :
            print("no informs")
