# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()
        # 关闭浏览器
        # self.driver.close()


    #平台类型
    def test_platformType(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('type').text
        self.assertTrue(u'人事' in tex)
        print tex

    #平台id
    def test_platformId(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('platformId').text
        self.assertTrue(u'HR_001' in tex)
        print tex

     #平台名称
    def test_platformname(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('name').text
        self.assertTrue(u'HR_001' in tex)
        print tex

     #平台版本
    def test_platformVersion(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('name').text
        self.assertTrue(u'0.3.1.beta' in tex)
        print tex

    #平台地址
    def test_platformaddress(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('address').text
        self.assertTrue(u'http://192.168.3.31:9030/hr' in tex)
        print tex

   #平台启动时间
    def test_platform_startTime(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('startTime').text
        self.assertTrue(u'2014-12-04 09:43:24' in tex)
        print tex

    #平台描述
    def test_platform_memo(self):
        #点击平台信息
        self.driver.find_element_by_id('helpInfo').click()
        tex=self.driver.find_element_by_id('memo').text
        self.assertTrue(u'HR人事子平台_001' in tex)
        print tex

