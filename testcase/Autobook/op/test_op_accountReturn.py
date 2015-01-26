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

    def test_createAccount(self):
        '''
        添加账号页面，点击返回按钮，回到账号管理页面
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        self.assertEqual(self.driver.title,u'添加账号')
        self.driver.find_id('return_btn').click()
        self.assertEqual(self.driver.title,u'账号管理',u'没有进入账号管理页面')
