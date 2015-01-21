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

    def test_createOperator2(self):
        '''
        添加已经存在的账号，系统提示'该用户已经存在'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_name').send_keys(u'lishan')
        self.driver.find_id('operator_realName').send_keys(u'李三')
        self.driver.find_id('operator_mobile').send_keys(u'18155364561')
        self.driver.find_id('sure_create_account_btn').click()
        text=self.driver.switch_to_alert().text
        self.assertTrue(u'该用户已经存在' in text)
        self.driver.switch_to_alert().accept()