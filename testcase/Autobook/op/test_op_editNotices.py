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

    def test_editNotice1(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        tds=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')
        tds[len(tds)-1].find_element_by_link_text(u'修改').click()
        self.driver.find_id('notice_title').clear()
        self.driver.find_id('notice_content').clear()
        self.driver.find_id('sure_btn').click()
        text1=self.driver.find_id('notice_title_tip').text
        text2=self.driver.find_id('notice_content_tip').text
        text3=self.driver.find_id('roleList_tip').text
        self.assertTrue(u'公告标题不能为空' in text1)
        self.assertTrue(u'公告内容不能为空' in text2)
        self.assertTrue(u'用户角色不能为空' in text3)



    def test_editNotice2(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/ul/li[5]/a').click()
        tds=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')
        tds[len(tds)-1].find_element_by_link_text(u'修改').click()
        self.driver.find_id('notice_title').clear()
        self.driver.find_id('notice_title').send_keys(u'最新消息')
        self.driver.find_id('notice_content').clear()
        t=u'现将2015年寒假放假相关事宜通知如下: 一、放假时间 1.学生:1月24日~2月28日。3月1日报到注册,3月2日正式上课。 2.教职工:1月25日~2月28日。1月24日、3月1日正常上班。'
        self.driver.find_id('notice_content').send_keys(t)

        self.driver.find_id('sure_btn').click()
        tds=self.driver.find_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')
        title=tds[1].text
        content=tds[2].text
        self.assertEqual(u'最新消息',title)
        self.assertEqual(t,content)

