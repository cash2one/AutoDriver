# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
import unittest
from framework.core import idriver_web


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        #登录平台
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
        time.sleep(5)
         #关闭浏览器
        self.driver.close()

    def test_setting_reset(self):
       #点击系统公告
       self.driver.find_id('sysNotice').click()
       nametx= self.driver.find_id('name').text
       print nametx
       #点击未读
       self.driver.find_id('unread').click()
       contx=self.driver.find_id('content').text
       print contx