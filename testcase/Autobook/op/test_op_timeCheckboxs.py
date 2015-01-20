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

    def test_sourceOrder(self):
        '''
        按时段统计订单，查看订单来源及订单类型下拉框
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        self.driver.find_id('li_time').click()
        opts=self.driver.find_id('orderSource_time').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'全部')
        #订单来源默认显示全部
        tuple=(u'全部',u'平台下单',u'客户下单',u'微信下单')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,'false')


    def test_orderType(self):
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('orderType_time').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'全部')
        #订单类型默认显示全部
        tuple=(u'全部',u'指定下单',u'周边下单')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,'false')
        #查看订单类型下拉框中的选项


    def test_dateControl(self):
        '''
        结束时间小于开始时间，系统给出错误提示
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()
        self.driver.find_id('li_time').click()
        js = '$(\'input[id=startTime_time]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime_time').clear()
        self.driver.find_element_by_id('startTime_time').send_keys('2015-01-06')
        #选择开始时间
        js = '$(\'input[id=endTime_time]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime_time').clear()
        self.driver.find_element_by_id('endTime_time').send_keys('2015-01-01')
        self.driver.find_id('statistics_time').click()
        #选择结束时间
        time.sleep(3)
        text=self.driver.switch_to_alert().text
        self.assertEqual(text,u'开始时间不能大于截止时间，请重新选择！')
        self.driver.switch_to_alert().accept()
        print(text)
