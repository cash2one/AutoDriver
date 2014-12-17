# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户未登录，填写手机号码界面，手机号为空
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
       #点击我的信息
       #self.driver.find_id('personal_name').click()
       #点击我的信息
       self.driver.find_ids('person_item')[0].click()
       #在填写手机号界面点击下一步
       self.driver.find_id('next_step').click()
       self.driver.switch_to_alert()
       text=self.driver.find_id('tv_msg').text
       print text
       self.assertTrue(u'请填写手机号！' in text,'msg')
