__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.files import *
from util import location
from util import mobile
from util import location

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.url='http://112.124.117.108/'
        self.ff.get(self.url)
        # m=mobile.android('')
        # self.dr=location.Location(m)

        self.loc=location.Location(self.ff)
        self.ff.get_cookie('username')


    def tearDown(self):
        self.ff.quit()

    def test_find_qq(self):

        self.loc.findTagNames('ul').findLinkText('blog').click()
        self.ff.find_element_by_id('help').click()

        try:
            self.assertTrue('http://112.124.117.108/blog/' in self.ff.current_url)
            # about_text=self.ff.find_element_by_id('helpNav').find_elements_by_tag_name('li')[0].text
            # self.assertTrue(u'新手入门' in about_text)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'report'+os.sep+'geweg.png')
            pass


if __name__ =='__main__':
    unittest.main()