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

    def test_queryRole1(self):
        '''
        查询条件角色类型为客服,列表中显示相应数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()
        opts=self.driver.find_id('platformType').find_tags('option')
        self.assertTrue(opts[0].text==u'全部角色')
        for opt in opts:
            if opt.get_attribute('text')==u'客服':
                opt.click()
                self.assertTrue(opt.is_selected())
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[1].text
                self.assertEqual(text,u"客服")
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

    def test_queryRole2(self):
        '''
        查询不存在的角色，列表中显示'没有符合条件的数据'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()

        self.driver.find_id('roleInfo').send_keys(u'jfsdkjf')
        self.driver.find_id('query').click()
        text=self.driver.find_class('norecords').text
        self.assertTrue(u'没有符合条件的数据'in text)

    def test_queryRole3(self):
        '''
        查询条件角色类型为客服，名称为服务员，列表中显示相应数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'角色管理').click()

        self.driver.find_id('roleInfo').send_keys(u'管理员')
        opts=self.driver.find_id('platformType').find_tags('option')
        self.assertTrue(opts[0].text==u'全部角色')
        for opt in opts:
            if opt.get_attribute('text')==u'客服':
                opt.click()
                self.assertTrue(opt.is_selected())
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                type=trs[i].find_tags('td')[1].text
                self.assertEqual(type,u"客服")
                name=trs[i].find_tags('td')[2].text
                self.assertTrue(u'管理员' in name)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)