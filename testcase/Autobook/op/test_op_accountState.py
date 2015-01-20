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

    def test_stateQuery(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'账号管理').click()
        opts=self.driver.find_id('state').find_elements_by_tag_name('option')

        for opt in opts:
            if opt.get_attribute('text')==u'全部':
                opt.click()
                self.assertTrue(opt.is_selected())
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_elements_by_tag_name('tr')
        for i in range(1,len(trs)):
            tds=trs[i].find_elements_by_tag_name('td')
            text=tds[4].text
            if text==u'已禁用':
                self.assertTrue(tds[len(tds)-1].find_elements_by_link_text(u'启用'))
            else:
                self.assertTrue(tds[len(tds)-1].find_elements_by_link_text(u'禁用'))
            self.assertTrue(tds[len(tds)-1].find_elements_by_link_text(u'编辑'))
            self.assertTrue(tds[len(tds)-1].find_elements_by_link_text(u'重置密码'))
        #状态为已禁用的，操作栏显示：编辑、启用、重置密码
        #状态为正常的，操作栏显示：编辑、禁用、重置密码