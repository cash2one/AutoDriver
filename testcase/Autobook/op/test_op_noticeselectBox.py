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

    def test_noticeName1(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()

        self.driver.find_id('create').click()
        self.driver.find_id('allRole').click()
        time.sleep(3)
        try:
            inputs=self.driver.find_id('roleList').find_elements_by_tag_name('input')
            for ipt in inputs:
                self.assertTrue(ipt.is_selected())
        finally:
            pass
        #点击全部角色，全部角色被选中

    def test_noticerole2(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()

        self.driver.find_id('create').click()
        self.driver.find_id('platform2').find_elements_by_tag_name('input')[0].click()

        time.sleep(3)
        try:
            inputs=self.driver.find_id('pf2_roles').find_elements_by_tag_name('input')
            for ipt in inputs:
                self.assertTrue(ipt.is_selected())
        finally:
            pass
        #点击全部客服，全部客服角色被选中