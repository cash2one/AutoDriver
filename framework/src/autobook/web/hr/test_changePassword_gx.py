__author__ = 'gaoxu@pathbook.com.cn'
# coding=utf-8

import time
import unittest
from framework.core import idriver_web


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        #登录平台
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
        time.sleep(5)
         #关闭浏览器
        self.driver.close()

     #内容为空
    def test_password_null(self):
       #点击个人设置
        self.driver.find_id('myNes').click()
        menu=self.driver.find_class_name('tab_head')

        menu.driver.find_class_name('tab_head_show').click()
        print menu
        # menu.driver.find_class_name(u'修改密码').click()

       #清空文本框的内容
        self.driver.find_id('oldPassword').clear()
        self.driver.find_id('input_text_C').clear()
        self.driver.find_id('confirmPassword').clear()
        #点击提交按钮
        self.driver.find_id('passSubmit').click()
        realnametx=self.driver.find_id('oldPassword_tip').text
        self.assertTrue(u'原密码不能为空.' in realnametx)
        print realnametx
        mobile_tiptx=self.driver.find_id('newPassword_tip').text
        self.assertTrue(u'新密码不能为空.' in mobile_tiptx)
        print mobile_tiptx
        email_tiptx=self.driver.find_id('confirmPassword_tip').text
        self.assertTrue(u'确认密码不能为空.' in email_tiptx)
        print email_tiptx
