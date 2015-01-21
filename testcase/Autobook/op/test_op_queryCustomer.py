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

    def test_queryCustomer(self):
        '''
        编辑客户来源及时间范围，列表中显示的是统计条件下的客户数目
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        opts=self.driver.find_id('customerSource').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'平台注册':
                opt.click()
                self.assertTrue(opt.is_selected())

        js = '$(\'input[id=startTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime').clear()
        self.driver.find_element_by_id('startTime').send_keys('2015-01-06')
        #选择开始时间
        js = '$(\'input[id=endTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime').clear()
        self.driver.find_element_by_id('endTime').send_keys('2015-01-17')
        #选择结束时间
        self.driver.find_id('statistics').click()
        time.sleep(3)
        text=self.driver.find_element_by_id('customerSource').text
        time1=self.driver.find_element_by_id('time1').text
        time2=self.driver.find_element_by_id('time2').text

        self.assertTrue(u'平台注册' in text)
        #列表显示平台注册的客户数目
        print time1,time2
        self.assertEqual(time1,'20150106')
        self.assertEqual(time2,'20150117')
        #列表显示查询时间段的


    def test_queryCustomer1(self):
        '''
        时间粒度选择按月，列表按月显示客户新增数目
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()
        opts=self.driver.find_id('dateType').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'按月':
                opt.click()
                self.assertTrue(opt.is_selected())

        Syears=self.driver.find_id('startYear').find_elements_by_tag_name('option')
        for Syear in Syears:
            if Syear.get_attribute('text')==u'2014':
                Syear.click()
                self.assertTrue(Syear.is_selected())

        Smonths=self.driver.find_id('startMonth').find_elements_by_tag_name('option')
        for Smonth in Smonths:
            if Smonth.get_attribute('text')==u'10':
                Smonth.click()
                self.assertTrue(Smonth.is_selected())

        Eyears=self.driver.find_id('endYear').find_elements_by_tag_name('option')
        for Eyear in Eyears:
            if Eyear.get_attribute('text')==u'2015':
                Eyear.click()
                self.assertTrue(Eyear.is_selected())

        Emonths=self.driver.find_id('endMonth').find_elements_by_tag_name('option')
        for Emonth in Emonths:
            if Emonth.get_attribute('text')==u'01':
                Emonth.click()
                self.assertTrue(Emonth.is_selected())
        #时间粒度选择‘按月’
        self.driver.find_id('statistics').click()

        time1=self.driver.find_element_by_id('time1').text
        time2=self.driver.find_element_by_id('time2').text


        self.assertEqual(time1,'201410')
        self.assertEqual(time2,'201501')










