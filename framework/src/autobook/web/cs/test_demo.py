__author__ = 'guguohai@pathbook.com.cn'
# coding=utf-8

import unittest
from framework.core import device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = device.app('idriver.web.cs', device.firefox)

    def tearDown(self):
        pass

    def test_list1(self):
        self.ff.get('http://www.w3school.com.cn/')
        txt = self.ff.find_elements_by_id('h').text

        self.assertTrue(u'HTML 系列教程' in txt ,'false')


    def test_list2(self):
        self.ff.get('http://www.w3school.com.cn/')
        #txt = self.ff.find_id('w3').find_tag('h2').text
        print self.ff.find_id('w3')
        print self.ff.find_tag('h2')
        txt = self.ff.find_element_by_id('w3').find_element_by_tag_name('h2').text


        self.assertTrue(u'领先的 Web 技术教程 - 全部免费' in txt , 'false')