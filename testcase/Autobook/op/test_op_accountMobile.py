# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_mobileNull(self):
        '''
        添加账号时，手机号码不输入，提交时系统提示’手机号码不能为空‘
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_name').send_keys(u'lishan1')
        self.driver.find_id('operator_realName').send_keys(u'李三1')
        self.driver.find_id('sure_create_account_btn').click()
        mobile=self.driver.find_id('operator_mobile_tip').text
        self.assertTrue(u'手机号码不能为空' in mobile)

    def test_mobileError(self):
        '''
        手机号码输入长度不对及输入非法字符，系统提示'手机号码输入错误,请输入11位手机号码.'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_name').send_keys(u'lishan1')
        self.driver.find_id('operator_realName').send_keys(u'李三1')
        self.driver.find_id('operator_mobile').send_keys(u'1815536')
        self.driver.find_id('sure_create_account_btn').click()
        mobile=self.driver.find_id('operator_mobile_tip').text
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.'in mobile,u'提示不正确或没有提示')

        self.driver.find_id('operator_mobile').clear()
        self.driver.find_id('operator_mobile').send_keys(u'gjkfsjgkljsssss')
        self.driver.find_id('sure_create_account_btn').click()
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.'in mobile,u'提示不正确或没有提示')

        self.driver.find_id('operator_mobile').clear()
        self.driver.find_id('operator_mobile').send_keys('<td>')
        self.driver.find_id('sure_create_account_btn').click()
        self.assertTrue(u'手机号码输入错误,请输入11位手机号码.'in mobile,u'提示不正确或没有提示')