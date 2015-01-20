# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

     #内容为空
    def test_password_null(self):
       #点击个人设置
        self.driver.find_id('myNes').click()
        menu=self.driver.find_class_name('tab_head')

        me= menu.driver.find_class_name('tab_head_show').click()
        self.assertTrue(me.is_selected())
        print menu
        # menu.driver.find_class_name(u'修改密码').click()

       #清空文本框的内容
        self.driver.find_element_by_id('oldPassword').clear()
        self.driver.find_element_by_id('input_text_C').clear()
        self.driver.find_element_by_id('confirmPassword').clear()
        #点击提交按钮
        self.driver.find_element_by_id('passSubmit').click()
        realnametx=self.driver.find_element_by_id('oldPassword_tip').text
        self.assertTrue(u'原密码不能为空.' in realnametx)
        print realnametx
        mobile_tiptx=self.driver.find_element_by_id('newPassword_tip').text
        self.assertTrue(u'新密码不能为空.' in mobile_tiptx)
        print mobile_tiptx
        email_tiptx=self.driver.find_element_by_id('confirmPassword_tip').text
        self.assertTrue(u'确认密码不能为空.' in email_tiptx)
        print email_tiptx
