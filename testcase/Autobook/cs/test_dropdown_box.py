__author__ = 'wangshasnhan'
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import atexit
from util.fileUtil import *

class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff=webdriver.Firefox()
        self.url="http://112.124.117.108/tupu/table/"
        self.ff.maximize_window()
        time.sleep(1)


    def tearDown(self):
        time.sleep(1)
        self.ff.quit()

    def test_box(self):
        self.ff.get(self.url)
        opts=self.ff.find_element_by_id('select_value').find_elements_by_tag_name('option')
        for opt in opts:
             if opt.get_attribute('value')=='three':
                 opt.click()
        try:
            self.assertTrue('http://112.124.117.108/tupu/table/' in self.ff.current_url)
        finally:
            pass



    def test_link(self):
        self.ff.get(self.url)
        self.ff.find_element_by_link_text('back').click()
        try:
            self.assertTrue('http://112.124.117.108/tupu/' in self.ff.current_url)
        finally:
            pass


    def test_text(self):
        self.ff.get(self.url)
        inp=self.ff.find_element_by_tag_name('input')
        inp.send_keys('fwefewfew')
        print self.ff.find_element_by_tag_name('h1').text
        print inp.get_attribute("value")

















