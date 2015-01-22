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

    def test_selectLimit(self):
        '''
        添加角色页面，点击复选框，复选框被选中，再次点击，复选框被取消选中
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        els=self.driver.find_id('lv1Menu20').find_tags('input')[0]
        els.click()
        self.assertTrue(els.is_selected())
        time.sleep(3)
        els.click()
        self.assertFalse(els.is_selected())


