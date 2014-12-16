# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户登录，查看如何收费界面
import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #查看如何收费
       self.driver.find_ids('person_item')[2].click()

       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'如何收费' in text,'msg')
       #点击左上角返回按钮
       self.driver.find_id('button_title_back').click()
