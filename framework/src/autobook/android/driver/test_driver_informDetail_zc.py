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

    def test_inform(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity
        try:
            el=self.driver.find_id('tv_msg_count')
            if el.is_displayed():
                self.driver.find_id("iv_head").click()
                self.driver.wait_switch(current_activity)
                text1=self.driver.find_id("personal_msg_count").text
                current_activity = self.driver.current_activity
                self.driver.find_element_by_name(u"消息公告").click()
                self.driver.wait_switch(current_activity)

                txt=self.driver.find_id('bulletin_text').text
                title1=txt.split(" ")[1]

                current_activity = self.driver.current_activity
                self.driver.find_id('bulletin_text').click()
                self.driver.wait_switch(current_activity)

                title2=self.driver.find_id('tv_title_text').text

                # current_activity = self.driver.current_activity
                # self.driver.find_elements_by_class_name('android.widget.Button')[0].click()
                # self.driver.wait_switch(current_activity)
                self.driver.back()

                text2=self.driver.find_id("personal_msg_count").text

                # self.assertTrue(title1==title2)
                # self.assertTrue(content1==content2)
                # self.assertTrue(text1==text2)
                print text1,title1,title2,text2

            else:
                pass

        except :
            print ("fdf")


