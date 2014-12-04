# coding=utf-8

__author__ = 'wangsahnshan@126.com'
#用户登录，联系电话为空（若不为空，删除电话号码）

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



       #点击一键下单按钮跳转到一键下单界面
       self.driver.find_id('rb_order').click()

       #删除联系电话
       self.driver.clear_text('tv_phone')
       self.driver.find_id('tv_phone').send.keys('13636468713')



       #点击立即下单
       #self.driver.find_id('bt_order').click()
       #跳转到填写手机号界面
       #txt1=self.driver.find_id('tv_title_text').text
       #print txt1
       #self.assertTrue(u'填写手机号' in txt1,'msg')
