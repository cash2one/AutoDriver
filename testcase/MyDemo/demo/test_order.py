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

        :return:
        '''
        #print sys._getframe().f_code.co_name

        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'您的爱车代驾首选' in u'您的爱车', self.issue(self.func_name(),u'不存在指定字符串'))

    def test_print_b(self):
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'您的爱车代驾首选' in u'您的爱车', self.issue(u'不存在指定字符串'))

    def test_print_c(self):
        # slogan = self.driver.find_element_by_class_name('slogan').text
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'您的爱车代驾首选' in u'您的爱车', self.issue(u'不存在指定字符串'))