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
            #若有未读标志则进行if流程，点击图标
            if el.is_displayed():
                text1=el.text
                self.driver.find_id("iv_head").click()
                self.driver.wait_switch(current_activity)

                current_activity = self.driver.current_activity
                count_id=self.driver.find_id('personal_msg_count')
                msg_count1=self.driver.find_id('personal_msg_count').text
                #查看未读公告前的未读条数
                self.driver.find_element_by_name(u"消息公告").click()
                self.driver.wait_switch(current_activity)
                red=self.driver.find_ids('bulletin_read')[0]
                current_activity = self.driver.current_activity

                self.driver.find_ids('bulletin_text')[0].click()
                #查看列表中第一条未读公告
                self.driver.wait_switch(current_activity)
                self.driver.find_element_by_class_name('android.widget.Button').click()

                if text1==unicode(1):
                #只有一条未读公告时，查看未读公告后，未读标志消失
                    self.assertFalse(red.is_displayed())
                #查看完未读公告后，公告前的红色标志消失
                    self.assertFalse(count_id.is_displayed())

                else :
                #有多条未读公告时，查看一条未读公告后，未读条数-1
                    self.driver.find_id('button_title_back').click()
                    self.driver.wait_switch(current_activity)
                    msg_count2=self.driver.find_id('personal_msg_count').text
                    self.assertTrue(int(msg_count1)-int(msg_count2)==1)
        except:
            #没有未读公告时，打印
            print ('no informs')





