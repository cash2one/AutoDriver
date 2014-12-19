# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import idriver_android


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()
    #一键下单界面，更改所在位置
    def test_change_Address(self):
        current_activity = self.driver.current_activity
        #点击一键下单，进入一键下单界面
        self.driver.find_id('rb_order').click()
        #点击所在位置
        self.driver.find_id('bt_address').click()
        #清空所在位置输入框
        self.driver.find_id('iv_delete').click()
        #输入新的地址
        self.driver.find_id('et_search').send_keys('hechuanlu')
        self.driver.wait_switch(current_activity)
        self.driver.switch_to_alert()

        addressinput_text = self.driver.find_tags('LinearLayout')[1].text
        self.driver.find_tags('LinearLayout')[1].click()
        address_text = self.driver.find_id('bt_address').text
        #判断是否是所选地址
        self.assertTrue(addressinput_text in address_text)



