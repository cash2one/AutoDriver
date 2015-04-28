# coding=utf-8

__author__ = 'wangsahnshan@126.com'


import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        #self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_change_Personal(self):
       '''
       用户登录，验证码输入错误
       :return:
       '''

       #点击进入使用
       # self.driver.find_id('start_btn').click()
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #点击我的信息
       self.driver.find_ids('person_item')[0].click()
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
