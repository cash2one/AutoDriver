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




        text1=self.driver.find_id('tv_msg_count').text
        self.driver.find_id("iv_head").click()
        self.driver.wait_switch(current_activity)

        current_activity = self.driver.current_activity
        msg_count1=self.driver.find_id('personal_msg_count')
        self.driver.find_element_by_name(u"消息公告").click()
        self.driver.wait_switch(current_activity)
        red=self.driver.find_element_by_class_name('android.widget.ListView').find_elements_by_class_name('android.widget.LinearLayout')[0].find_element_by_id('bulletin_read')
        current_activity = self.driver.current_activity

        self.driver.find_ids('bulletin_text')[0].click()
        self.driver.wait_switch(current_activity)

        self.driver.find_element_by_class_name('android.widget.Button').click()

        self.assertFalse(red.is_displayed())
        self.driver.find_id('button_title_back').click()
        self.driver.wait_switch(current_activity)
        print text1,unicode(1)

        # if text1==unicode(1):
        #
        #     self.assertFalse(msg_count1.is_displayed())
        # else :
        #     msg_count2=self.driver.find_id('personal_msg_count')
        #     print int(msg_count1.text)-int(msg_count2.text)

        # try:
        #     el=self.driver.find_id('tv_msg_count')
        #     if el.is_displayed():
        #         text1=el.text
        #         self.driver.find_id("iv_head").click()
        #         self.driver.wait_switch(current_activity)
        #
        #         current_activity = self.driver.current_activity
        #         msg_count1=self.driver.find_id('personal_msg_count').text
        #         self.driver.find_element_by_name(u"消息公告").click()
        #         self.driver.wait_switch(current_activity)
        #         red=self.driver.find_ids('bulletin_read')[0]
        #         current_activity = self.driver.current_activity
        #
        #         self.driver.find_ids('bulletin_text')[0].click()
        #         self.driver.wait_switch(current_activity)
        #
        #         self.driver.find_element_by_class_name('android.widget.Button').click()
        #         self.driver.wait_switch(current_activity)
        #         self.assertFalse(red.is_displayed())
        #         self.driver.find_id('button_title_back').click()
        #         self.driver.wait_switch(current_activity)
        #         msg_count2=self.driver.find_id('personal_msg_count').text
        #
        #         if text1==1:
        #             self.assertFalse(msg_count2.is_displayed())
        #         else :
        #             print int(msg_count1)-int(msg_count2)
        # except:
        #     print ('no')





