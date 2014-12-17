# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户未登录，直接一键下单

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
       #页面加载等待时间
       self.driver.wait_loading()
       #点击一键下单
       self.driver.find_id('rb_order').click()
       #判断是否是一键下单界面
       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'一键下单' in text,'msg')
       #点击立即下单
       self.driver.find_id('bt_order').click()
       #跳转到填写手机号
       text1=self.driver.find_id('tv_title_text').text
       print text1
       self.assertTrue(u'填写手机号' in text1,'msg')

