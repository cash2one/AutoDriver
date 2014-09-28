# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'


from selenium import webdriver
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()

    def tearDown(self):
        self.ff.quit()

    def test_list1(self):
        self.ff.get('http://112.124.117.108/tupu/table/')

        trs=self.ff.find_element_by_id('tableid').find_elements_by_tag_name('tr')
        con = trs[0].find_elements_by_tag_name('th')[0].text
        self.assertTrue('naa' in con,u'未发现指定字符')
