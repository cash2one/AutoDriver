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
    def test_setting_null(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        nametx=self.driver.find_element_by_id('name').text
        print nametx
       #清空文本框的内容
        self.driver.find_element_by_id('realName').clear()
        self.driver.find_element_by_id('mobile').clear()
        self.driver.find_element_by_id('email').clear()
        #点击提交按钮
        self.driver.find_element_by_id('infoSubmit').click()
        realnametx=self.driver.find_element_by_id('realName_tip').text
        self.assertTrue(u'真实姓名不能为空.' in realnametx)
        print realnametx
        mobile_tiptx=self.driver.find_element_by_id('mobile_tip').text
        self.assertTrue(u'手机不能为空.' in mobile_tiptx)
        print mobile_tiptx
        email_tiptx=self.driver.find_element_by_id('email_tip').text
        self.assertTrue(u'邮箱不能为空.' in email_tiptx)
        print email_tiptx

          #清空文本框的内容，电话错误
    def test_setting_phoneError(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        nametx=self.driver.find_element_by_id('name').text
        print nametx
        self.driver.find_element_by_id('realName').clear()
        self.driver.find_element_by_id('realName').send_keys(u'张静123abcdef')
        self.driver.find_element_by_id('mobile').clear()
        self.driver.find_element_by_id('mobile').send_keys('abc123123')
        self.driver.find_element_by_id('email').clear()
        self.driver.find_element_by_id('email').send_keys(u'zhang123@163.com')
        #点击提交按钮
        self.driver.find_element_by_id('infoSubmit').click()
        #错误提示
        motx=self.driver.find_element_by_id('mobile_tip').text
        self.assertTrue(u'手机输入错误,请输入11位手机号码.' in motx)

        #清空文本框的内容，邮箱错误
    def test_setting_emileError(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        nametx=self.driver.find_element_by_id('name').text
        print nametx
        self.driver.find_element_by_id('realName').clear()
        self.driver.find_element_by_id('realName').send_keys(u'张静123abcdef')
        self.driver.find_element_by_id('mobile').clear()
        self.driver.find_element_by_id('mobile').send_keys('13123456789')
        self.driver.find_element_by_id('email').clear()
        self.driver.find_element_by_id('email').send_keys(u'zhan.163.cm')
        #点击提交按钮
        self.driver.find_element_by_id('infoSubmit').click()
        emtx=self.driver.find_element_by_id('email_tip').text
        self.assertTrue(u'邮箱格式不正确.' in emtx)
        print emtx
        time.sleep(3)

     #清空文本框的内容，输入正确的参数
    def test_setting_correct(self):
       #点击个人设置
        self.driver.find_element_by_id('myNes').click()
        nametx=self.driver.find_element_by_id('name').text
        print nametx
        self.driver.find_element_by_id('realName').clear()
        self.driver.find_element_by_id('realName').send_keys(u'张静')
        self.driver.find_element_by_id('mobile').clear()
        self.driver.find_element_by_id('mobile').send_keys('13112345678')
        self.driver.find_element_by_id('email').clear()
        self.driver.find_element_by_id('email').send_keys(u'zhang123@163.com')
        #点击提交按钮
        self.driver.find_element_by_id('infoSubmit').click()
