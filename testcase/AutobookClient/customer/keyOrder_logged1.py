# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'
#用户未登录，一键下单界面，输入联系电话跳转到填写手机号码界面

import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        #self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    #联系电话输入小于11位
    def test_keyOrder_logged(self):

       # #点击进入使用
       # self.driver.find_id('start_btn').click()
       #页面加载等待时间
       self.driver.wait_loading()
       #点击一键下单
       self.driver.find_id('rb_order').click()
       #判断是否是一键下单界面
       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'一键下单' in text,'msg')
       #判断联系电话是否为空
       phoneNull=self.driver.find_id('tv_phone').text
       if len(phoneNull.strip())==0:
          self.driver.find_id('tv_phone').send_keys('136364687')
       phone=self.driver.find_id('tv_phone').text
       print phone
       #点击立即下单
       self.driver.find_id('bt_order').click()
       #跳转到填写手机号界面
       phone2=self.driver.find_id('phonenumber').text
       print phone2
       self.assertTrue(phone==phone2,'msg')


    #联系电话输入大于14位，系统限制输入（输入15位）
    def test_keyOrder_logged1(self):

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
       #判断联系电话是否为空
       phoneNull=self.driver.find_id('tv_phone').text
       if len(phoneNull.strip())==0:
          self.driver.find_id('tv_phone').send_keys('136364687132645')
       phone=self.driver.find_id('tv_phone').text
       print phone
       #点击立即下单
       self.driver.find_id('bt_order').click()
       #跳转到填写手机号界面
       phone2=self.driver.find_id('phonenumber').text
       print phone2
       self.assertTrue(phone2 in phone,'msg')



    #联系电话输入大于11位，（输入13位）
    def test_keyOrder_logged2(self):

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
       #判断联系电话是否为空
       phoneNull=self.driver.find_id('tv_phone').text
       if len(phoneNull.strip())==0:
          self.driver.find_id('tv_phone').send_keys('1363646871326')
       phone=self.driver.find_id('tv_phone').text
       print phone
       #点击立即下单
       self.driver.find_id('bt_order').click()
       #跳转到填写手机号界面
       phone2=self.driver.find_id('phonenumber').text
       print phone2
       self.assertTrue(phone2 in phone,'msg')

