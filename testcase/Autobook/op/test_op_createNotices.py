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

    def test_addNotice(self):
        '''
        添加公告，添加成功后显示在列表第一项
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        self.driver.find_id('create').click()
        self.driver.find_id('notice_title').send_keys(u'公告通知')
        self.driver.find_id('notice_content').send_keys(u'最近，凤凰台风来袭，注意关好窗户，防止衣服被刮走。')
        self.driver.find_id('allRole').click()
        self.driver.find_id('sure_btn').click()
        tds=self.driver.find_id('list').find_tags('tr')[1].find_tags('td')
        title=tds[1].text
        content=tds[2].text
        self.assertEqual(u'公告通知',title,u'新增公告没有显示在列表第一项')
        self.assertEqual(u'最近，凤凰台风来袭，注意关好窗户，防止衣服被刮走。',content,u'新增公告显示在列表第一项')