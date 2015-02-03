# coding=utf-8
__author__ = 'xiaohengli@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    #查询分页
    def test_logall(self):
        '''
        点击首页，上一页的呈灰色
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #点击末一页，是点击左后一夜的图标变灰
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
         #点击首页
        self.driver.find_element_by_id('first_pager').click()
        time.sleep(1)
        #点击下一页
        self.driver.find_element_by_id('next_pager').click()
        time.sleep(1)
        #点击上一页
        self.driver.find_element_by_id('prev_pager').click()
    def test_logInput(self):
        '''
        在跳转至文本框中输入的数字小于当前共有页数,系统自动跳转到该页
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数
        self.driver.find_class('ui-pg-input').send_keys("1" + self.driver.keys().RETURN)


    def test_Inputdecimal(self):
        '''
        在跳转至文本框中输入小数,系统默认跳转到第一页
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数小数
        time.sleep(1)
        self.driver.find_class('ui-pg-input').send_keys("1.5" + self.driver.keys().RETURN)

    #输入非法字符
    def test_InputCharacters(self):
        '''
        在跳转至文本框中输入字母、非法字符,系统默认跳转到第一页
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数
        time.sleep(1)
        self.driver.find_class('ui-pg-input').send_keys("@@@" + self.driver.keys().RETURN)
        test=self.driver.find_class('ui-pg-input').get_attribute('value')
        self.assertEqual(test,'1',u'没有这个字符')

    def test_InputCharacter(self):
        '''
        在跳转至文本框中输入超长字符,系统限制输入
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #跳转页数
        time.sleep(1)
        se=self.driver.find_element_by_id('sp_1_pager').text
        self.driver.find_class('ui-pg-input').send_keys("11111111111" + self.driver.keys().RETURN)
        time.sleep(5)
        value=self.driver.find_class('ui-pg-input').get_attribute('value')

        self.assertEqual(value,se,u'没有这个字符')

