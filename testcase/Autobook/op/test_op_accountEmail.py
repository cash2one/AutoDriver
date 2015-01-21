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

    def test_email1(self):
        '''
        Email中输入非法字符，系统提示Email格式不正确
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_email').send_keys('<td>')
        self.driver.find_id('sure_create_account_btn').click()
        text=self.driver.find_id('operator_email_tip').text
        self.assertTrue(u'Email格式不正确' in text)

    def test_email2(self):
        '''
        Email中输入格式不正确，系统提示Email格式不正确
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_email').send_keys('dgfdgfdgdsdgfdgdgd')
        self.driver.find_id('sure_create_account_btn').click()
        text=self.driver.find_id('operator_email_tip').text
        self.assertTrue(u'Email格式不正确' in text)