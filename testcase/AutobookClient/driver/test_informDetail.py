# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
import unittest
from framework.core import idriver_android
import datetime


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_inform(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity

        try:
            el=self.driver.find_id('tv_msg_count')
            #若有未读标志则走if流程，查看公告的标题是否一致
            if el.is_displayed():
                self.driver.find_id("iv_head").click()
                self.driver.wait_switch(current_activity)

                current_activity = self.driver.current_activity
                self.driver.find_element_by_name(u"消息公告").click()
                self.driver.wait_switch(current_activity)

                txt=self.driver.find_id('bulletin_text').text
                title1=txt.split(" ")[2]

                current_activity = self.driver.current_activity
                self.driver.find_id('bulletin_text').click()
                self.driver.wait_switch(current_activity)

                title2=self.driver.find_id('tv_title_text').text
                self.assertTrue(title1==title2)

            else:
                pass

        except :
            print ("no informs")


