__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.files import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.url='http://www.qq.com'


    def tearDown(self):
        self.ff.quit()

    def test_find_qq(self):
        self.ff.get(self.url)
        #time.sleep(20)
        self.ff.find_element_by_id('newsH2').click()
        try:
            self.assertTrue('http://news.qq.com/' in self.ff.current_url)
            about_text=self.ff.find_element_by_id('siteNavPart1').find_element_by_tag_name('li').text
            self.assertTrue(u'腾讯网首页' in about_text)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'report'+os.sep+'geweg.png')
            pass


if __name__ =='__main__':
    unittest.main()