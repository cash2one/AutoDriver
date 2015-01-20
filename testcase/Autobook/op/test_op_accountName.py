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

    def test_createOperator1(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('sure_create_account_btn').click()
        name=self.driver.find_id('operator_name_tip').text
        realName=self.driver.find_id('operator_realName_tip').text
        self.assertTrue(u'用户名不能为空' in name)
        self.assertTrue(u'姓名不能为空' in realName)

    def test_createOperator2(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        self.driver.find_id('operator_name').send_keys(u'<td>')
        self.driver.find_id('operator_realName').send_keys(u'<td>')
        self.driver.find_id('sure_create_account_btn').click()
        name=self.driver.find_id('operator_name_tip').text
        realName=self.driver.find_id('operator_realName_tip').text
        self.assertTrue(u'用户名输入错误,请输入英文字母数字或下划线' in name)
        self.assertTrue(u'姓名含有非法符号' in realName)
