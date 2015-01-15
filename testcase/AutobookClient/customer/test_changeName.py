# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户登录，修改用户名

import time
import unittest
from framework.core import testcase

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #我的信息
       self.driver.find_ids('personal_name')[0].click()
      #修改用户名
       self.driver.clear_text('personal_user_name')
       self.driver.find_id('personal_user_name').send_keys('AutoTst1')
       # self.driver.find_id('personal_user_name').click()
       # self.driver.keyevent(67)


       time.sleep(3)

       #点击完成（修改成功）
       self.driver.find_id('personal_finish').click()
