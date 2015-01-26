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

    def test_monitoringRefresh(self):
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在司机监控上
        self.driver.find_element_by_link_text(u'司机监控').click()
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'空闲':
                opt.click()

        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')
        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[4].text
                self.assertTrue(text,u"空闲")
                print(text)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

    def test_Combination(self):
        '''
        输入司机工号/姓名/手机号，选择司机状态，点击查询
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在司机监控上
        self.driver.find_element_by_link_text(u'司机监控').click()
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'空闲':
                opt.click()
        self.driver.find_element_by_id('driverInfo').send_keys(u'14')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')
        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[1].text
                self.assertTrue(text,u"14")
                text=trs[i].find_tags('td')[4].text
                self.assertTrue(text,u"空闲")
                print(text)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_Drivermonitoringquery(self):
        '''
       列表中显示符合查询条件的所有在线司机的的监控记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        self.driver.find_id('query').click()

        self.driver.find_element_by_id('driverInfo').send_keys(u'140226')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[1].text
                self.assertEqual(text,u"140226",u'没有找到该司机工号')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

