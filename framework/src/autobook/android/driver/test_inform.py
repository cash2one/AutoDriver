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
            #若有未读标志，则走if流程
            if el.is_displayed():
                text1=el.text
                self.driver.find_id("iv_head").click()
                self.driver.wait_switch(current_activity)
                text2=self.driver.find_id("personal_msg_count").text
                self.driver.find_element_by_name(u"消息公告").click()
                self.driver.wait_switch(current_activity)
                red=self.driver.find_ids('bulletin_read')
                text3=len(red)
                self.assertTrue(text1==text2==unicode(text3))
                #未读条数与红色标记的数目一致
            else:
                pass
        except :
            self.driver.find_id("iv_head").click()
            self.driver.wait_switch(current_activity)
            self.driver.find_element_by_name(u"消息公告").click()
            txt=self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            self.assertTrue(u"当前没有消息提示" in txt)
            print("no informs")
            #若没有未读标志，公告列表页面则显示当前没有消息提示
