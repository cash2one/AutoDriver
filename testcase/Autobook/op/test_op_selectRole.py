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


    def test_createOperator(self):
        '''
        添加账号页面，选中角色复选框
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        self.driver.find_id('create').click()
        opts=self.driver.find_id('pf2_roles').find_tags('input')
        for opt in opts:
            if opt.get_attribute('title')==u'客服经理':

                opt.click()
                self.assertTrue(opt.is_selected())
                time.sleep(2)
                opt.click()
                self.assertFalse(opt.is_selected())