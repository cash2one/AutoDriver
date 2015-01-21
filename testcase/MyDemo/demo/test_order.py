# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import sys
from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        pass

    def tearDown(self):
        pass

    def test_print_a(self):
        '''
        期望结果写这里
        :return:
        '''

        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'您的爱车代驾首选' in u'您的爱车', u'不存在指定字符串')

    def test_print_b(self):
        '''
        期望结果写这里
        :return:
        '''
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'您的爱车代驾首选' in u'您的爱车', u'不存在指定字符串')

    def test_print_c(self):
        '''
        期望结果写这里
        :return:
        '''
        # slogan = self.driver.find_element_by_class_name('slogan').text
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'您的爱车代驾首选' in u'您的爱车', u'不存在指定字符串')