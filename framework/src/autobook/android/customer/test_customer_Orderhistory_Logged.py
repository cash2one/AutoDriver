# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户未登录，查看历史订单

import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        #self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):

       #点击进入使用
       self.driver.find_id('start_btn').click()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击历史订单
       self.driver.find_id('person_item')[1].click()
       # self.driver.find_tags('RelativeLayout')[2].click()
       #查看填写手机号界面
       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'填写手机号' in text,'msg')

