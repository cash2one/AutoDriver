# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'


from selenium import webdriver
import unittest
from framework.core import device

class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = device.web()

    def tearDown(self):
        self.ff.quit()

    def test_list1(self):
        self.ff.get('http://112.124.117.108/tupu/table/')

        table = self.ff.find_element_by_id('tableid')
        trs = table.find_elements_by_tag_name('tr')

        find_result = ''
        exp_result = 'ff1ad'

        for tr in trs:
            if tr.find_elements_by_tag_name('td'):
                tds = tr.find_elements_by_tag_name('td')
                for td in tds:
                    if td.text == exp_result:
                        find_result  = 'yes'
                        break

        self.assertTrue('yes' in find_result,'none')


