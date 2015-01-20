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
        self.driver.find_id('sure_btn').click()
        text1=self.driver.find_id('notice_title_tip').text
        text2=self.driver.find_id('notice_content_tip').text
        text3=self.driver.find_id('roleList_tip').text
        self.assertTrue(u'公告标题不能为空' in text1)
        self.assertTrue(u'公告内容不能为空' in text2)
        self.assertTrue(u'用户角色不能为空' in text3)

