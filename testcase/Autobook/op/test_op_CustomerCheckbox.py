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
        在客户统计页面，查看客户来源下拉框，下拉框显示'全部'、'平台注册'、'手机注册'、'微信注册'、'接口注册'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        opts=self.driver.find_id('customerSource').find_tags('option')
        self.assertTrue(opts[0].text==u'全部')
        #客户来源默认显示全部
        tuple=(u'全部',u'平台注册',u'手机注册',u'微信注册',u'接口注册')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break
        time.sleep(2)
        self.assertTrue(isExist,'false')
        #查看客户来源下拉框中的选项

    def test_dateType(self):
        '''
        在客户统计页面，查看时间粒度下拉框，下拉框显示'按天'、'按年'、'按月'
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'统计查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'客户统计').click()

        opts=self.driver.find_id('dateType').find_tags('option')
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
        self.assertTrue(isExist,'false')
        #查看时间粒度下拉框中的选项