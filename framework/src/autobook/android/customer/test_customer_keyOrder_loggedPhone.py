# coding=utf-8

__author__ = 'wangsahnshan@126.com'
#用户未登录，联系电话为空

import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()
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
       #判断联系电话为空
       if 'null'== self.driver.find_id('tv_phone').text:
            self.driver.find_id('tv_phone').send_keys('123456')

       #点击立即下单
       self.driver.find_id('bt_order').click()
       #跳转到填写手机号界面
       txt=self.driver.find_id('tv_title_text').text
       print txt
       self.assertTrue(u'填写手机号' in txt,'msg')
