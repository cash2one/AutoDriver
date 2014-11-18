# coding=utf-8

__author__ = 'wangsahnshan@126.com'
#用户未登录，指定司机下单（周边有司机）

import time
import unittest
from framework.core import idriver_android
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

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
        #去除加载
       self.driver.wait_loading()

       #点击附近司机列表
       self.driver.find_id('rb_maplist').click()
       #判断列表中是否有司机
       nearbyrivers = []
       try:
          nearbyrivers = self.driver.find_ids('nearbyriver')
       except NoSuchElementException:
            pass

       self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')
       #选择列表中的第一个司机
       self.driver.find_ids('nearbyriver')[0].click()
       #跳转到司机信息界面点击立即下单
       self.driver.find_id('driver_order').click()
       #跳转到填写手机号界面
       txt=self.driver.find_id('tv_title_text').text
       print txt
       self.assertTrue(u'填写手机号' in txt,'msg')







