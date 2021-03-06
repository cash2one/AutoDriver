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

    def test_orderSource(self):
        '''
        按数量统计订单页面，查看订单来源下拉框，下拉框显示'全部'、'平台下单'、'客户下单'、'微信下单'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('orderSource_amount').find_tags('option')
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
        self.assertTrue(isExist,u'下拉框选项没有被选中')
        #查看订单来源下拉框中的选项


    def test_orderType(self):
        '''
        查看订单类型下拉框，下拉框显示'全部'、'指定下单'、'周边下单'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('orderType_amount').find_tags('option')
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
        self.assertTrue(isExist,u'下拉框选项没有被选中')
        #查看订单类型下拉框中的选项


    def test_dateType(self):
        '''
        查看时间粒度下拉框，下拉框显示'按天'、'按年'、'按月'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'订单统计').click()

        opts=self.driver.find_id('dateType_amount').find_tags('option')
        self.assertTrue(opts[0].text==u'按天')
        #时间粒度默认显示全部
        tuple=(u'按天',u'按年',u'按月')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,u'下拉框选项没有被选中')
        #查看时间粒度下拉框中的选项



