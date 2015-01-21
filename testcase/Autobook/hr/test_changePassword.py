# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        # self.driver.switch_to_home()
        # 关闭浏览器
        self.driver.close()

     #内容为空
    def test_password_null(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]').click()
       #清空文本框的内容
        self.driver.find_element_by_id('oldPassword').clear()
        self.driver.find_element_by_id('newPassword').clear()
        self.driver.find_element_by_id('confirmPassword').clear()
        #点击提交按钮
        but=self.driver.find_element_by_id('passSubmit')
        but.click()
        realnametx=self.driver.find_element_by_id('oldPassword_tip').text
        self.assertTrue(u'原密码不能为空.' in realnametx)
        mobile_tiptx=self.driver.find_element_by_id('newPassword_tip').text
        self.assertTrue(u'新密码不能为空.' in mobile_tiptx)
        email_tiptx=self.driver.find_element_by_id('confirmPassword_tip').text
        self.assertTrue(u'确认密码不能为空.' in email_tiptx)


     #原密码错误
    def test_oldpassword_mismatching(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]').click()
       #清空文本框的内容
        self.driver.find_element_by_id('oldPassword').clear()
        self.driver.find_element_by_id('newPassword').clear()
        self.driver.find_element_by_id('confirmPassword').clear()
        #输入不匹配的原密码
        self.driver.find_element_by_id('oldPassword').send_keys(u'2316878dfdwd')
        self.driver.find_element_by_id('newPassword').send_keys(u'abc123')
        self.driver.find_element_by_id('confirmPassword').send_keys(u'abc123')
        #点击提交按钮
        self.driver.find_element_by_id('passSubmit').click()
        con_tiptx=self.driver.find_element_by_id('confirmPassword_tip').text
        self.assertTrue(u'原密码错误!' in con_tiptx)


     #新密码不匹配
    def test_newpassword_mismatching(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]').click()
       #清空文本框的内容
        self.driver.find_element_by_id('oldPassword').clear()
        self.driver.find_element_by_id('newPassword').clear()
        self.driver.find_element_by_id('confirmPassword').clear()
        #输入不匹配的原密码
        self.driver.find_element_by_id('oldPassword').send_keys(u'666666')
        self.driver.find_element_by_id('newPassword').send_keys(u'abc123')
        self.driver.find_element_by_id('confirmPassword').send_keys(u'123456')
        #点击提交按钮
        self.driver.find_element_by_id('passSubmit').click()
        con_tiptx=self.driver.find_element_by_id('confirmPassword_tip').text
        self.assertTrue(u'新密码和确认密码不一致.' in con_tiptx)