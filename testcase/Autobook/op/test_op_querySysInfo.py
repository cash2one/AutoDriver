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

    def test_querySysInfo1(self):
        '''
        查询条件状态选择接口配置，列表中显示相应数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统参数').click()
        opts=self.driver.find_id('paramType').find_tags('option')

        for opt in opts:
            if opt.get_attribute('text')==u'接口配置':
                opt.click()
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[1].text
                self.assertEqual(text,u"接口配置")
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_querySysInfo2(self):
        '''
        查询条件状态选择接口配置，列表中显示相应数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统参数').click()
        opts=self.driver.find_id('paramType').find_tags('option')

        for opt in opts:
            if opt.get_attribute('text')==u'后台配置':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')

        self.driver.find_id('sysInfo').send_keys(u'CORE')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                text1=trs[i].find_tags('td')[1].text
                text2=trs[i].find_tags('td')[2].text
                self.assertEqual(text1,u"后台配置")
                self.assertTrue(u"CORE" in text2)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_querySysInfo3(self):
        '''
        查询条件状填写参数描述，列表中显示相应数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统参数').click()
        opts=self.driver.find_id('paramType').find_tags('option')

        for opt in opts:
            if opt.get_attribute('text')==u'后台配置':
                opt.click()
                self.assertTrue(opt.is_selected(),u'下拉框选项没有被选中')

        self.driver.find_id('sysInfo').send_keys(u'http://192.168.3.31')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                text1=trs[i].find_tags('td')[1].text
                text2=trs[i].find_tags('td')[2].text
                self.assertEqual(text1,u"后台配置")
                self.assertTrue(u"http://192.168.3.31" in text2)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)