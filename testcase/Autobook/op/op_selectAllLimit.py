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

    def test_selectAllLimit(self):
        '''
        点击全选复选框，权限选项全部被选中
        点击反选复选框，权限选项全部被取消选中
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()
        #进入角色添加页面
        self.driver.find_id('allLimit').click()

        try:
            inputs=self.driver.find_id('limitsList').find_tags('input')
            for ipt in inputs:
                self.assertTrue(ipt.is_selected(),u'下拉框选项没有被选中')
        finally:
            pass


        self.driver.find_id('reverseCheck').click()
        #点击反选复选框，权限选项全部被取消选中
        try:
            inputs=self.driver.find_id('limitsList').find_tags('input')
            for ipt in inputs:
                self.assertFalse(ipt.is_selected())
        finally:
            pass