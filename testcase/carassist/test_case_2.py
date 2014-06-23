__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.url='http://www.pathbook.com.cn'


    def tearDown(self):
        self.ff.quit()

    def test_tupu(self):
        self.ff.get(self.url)
        self.ff.find_element_by_xpath('/html/body/div[2]/div/div[2]/a[2]').click()
        try:
            self.assertTrue('http://www.pathbook.com.cn/abouts.htm' in self.ff.current_url)
            about_text=self.ff.find_element_by_xpath('//*[@id="jieshaoDiv"]/h2').text
            self.assertTrue(u'途谱介绍' in about_text)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'report'+os.sep+'geweg.png')
            pass


if __name__ =='__main__':
    unittest.main()