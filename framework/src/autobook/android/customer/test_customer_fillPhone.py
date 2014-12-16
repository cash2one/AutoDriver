# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#填写手机号码界面输入少于11位的手机号
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
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击我的信息
       #self.driver.find_id('personal_name').click()
       self.driver.find_ids('person_item')[0].click()
       #输入少于11位的手机号
       self.driver.find_id('phonenumber').click()
       self.driver.find_id('phonenumber').send_keys('136364')
       #在填写手机号界面点击下一步
       self.driver.find_id('next_step').click()
       self.driver.switch_to_alert()
       text=self.driver.find_id('tv_msg').text
       print text
       self.assertTrue(u'手机号码格式不正确' in text,'msg')

