# coding=utf-8

__author__ = 'wangsahnshan@126.com'
# 用户未登录，在填写手机号页面输入少于11位的手机号码
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
       self.driver.find_id('btn_personalcenter').click()
       #点击我的信息
       self.driver.find_ids('personal_name')[0].click()
       #输入正确的手机号
       self.driver.find_id('phonenumber').click()
       self.driver.find_id('phonenumber').send_keys('18964086193')
       #在填写手机号界面点击下一步
       self.driver.find_id('next_step').click()
       #输入手机验证码
       self.driver.find_id('verification_code').click()
       self.driver.find_id('verification_code').send_keys('123456')
       #点击提交按钮
       self.driver.find_id('code_submit').click()
       #判断弹出框是否是校验失败
       self.driver.switch_to_alert()
       text=self.driver.find_id('tv_msg').text
       print text
       self.assertTrue(u'校验失败' in text,'msg')