# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

        #取消拨打客服电话
    def test_cancel(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity
        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)
        current_activity = self.driver.current_activity
        self.driver.find_id('button_title_function').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'温馨提示:是否拨打客服热线？' in txt)
        self.driver.find_id('btn_cancel').click()
        current_activity = self.driver.current_activity


        #确定拨打客服电话
    def test_confirm(self):
        self.driver.change_status(True)
        current_activity = self.driver.current_activity
        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)
        current_activity = self.driver.current_activity
        self.driver.find_id('button_title_function').click()
        self.driver.switch_to_alert()
        txt = self.driver.find_id('tv_msg').text
        self.assertTrue(u'温馨提示:是否拨打客服热线？' in txt)
        self.driver.find_id('btn_ok').click()
        current_activity = self.driver.current_activity

