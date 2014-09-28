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

        table = self.ff.find_element_by_id('tableid')
        tr = table.find_elements_by_tag_name('tr')

        th0 = tr[0].find_elements_by_tag_name('th')[0]
        txt = th0.text

        self.assertTrue('n' in txt,'none')


