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

    def test_dateControl(self):
        '''
        结束时间小于开始时间，系统给出错误提示
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        js = '$(\'input[id=startTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime_amount').clear()
        self.driver.find_element_by_id('startTime_amount').send_keys('2015-01-06')
        #选择开始时间
        js = '$(\'input[id=endTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime_amount').clear()
        self.driver.find_element_by_id('endTime_amount').send_keys('2015-01-01')
        self.driver.find_id('statistics_amount').click()
        #选择结束时间
        time.sleep(3)
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'开始日期不能大于结束时间，请重新选择！')
        self.driver.switch_to_alert().accept()
        print(text)

    def test_dateControl1(self):
        '''
        结束时间小于开始时间，系统给出错误提示
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        js = '$(\'input[id=startTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime_amount').clear()
        self.driver.find_element_by_id('startTime_amount').send_keys('2014-11-06')
        #选择开始时间
        js = '$(\'input[id=endTime_amount]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime_amount').clear()
        self.driver.find_element_by_id('endTime_amount').send_keys('2015-01-01')
        self.driver.find_id('statistics_amount').click()
        #选择结束时间
        time.sleep(3)
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'按天统计，只统计30天内的数据，请重新选择！')
        self.driver.switch_to_alert().accept()
        print(text)




