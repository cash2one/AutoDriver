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

    def test_roleType(self):
        '''
        添加角色时，查看角色类型下拉框，'客服'、'人事'、'财务'、'运维'、'接口'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        self.driver.find_id('create').click()

        opts=self.driver.find_id('role_platformType').find_tags('option')
        self.assertTrue(opts[0].text==u'客服')
        #角色类型默认显示客服
        tuple=(u'客服',u'人事',u'财务',u'运维',u'接口')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break

        self.assertTrue(isExist,'false')
        #查看角色类型下拉框中的选项


