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

    def test_sameName(self):
        '''
        添加已存在的角色，系统提示'该用户已经存在!'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.driver.find_id('role_name').send_keys(u'财务超级管理8')
        self.driver.find_id('sure_create_role_btn').click()
        name=self.driver.switch_to_alert().text

        self.assertEqual(name,u'该用户已经存在!')
        self.driver.switch_to_alert().accept()