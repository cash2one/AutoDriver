# coding=utf-8

__author__ = 'Administrator'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.customer')
        idriver.login_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击用户中心
       self.driver.find_id('btn_personalcenter').click()
       #点击我的信息
       self.driver.find_id('personal_name').click()
       #清除用户名

       self.driver.clear_text('personal_user_name')
       self.driver.find_element_by_id(pkg+'personal_user_name').send_keys(user_name)