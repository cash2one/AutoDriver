__author__ = 'Administrator'
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from util.files import *
import os

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        #self.ff.implicitly_wait(10) #设置网页打开超时时间

    def tearDown(self):
        self.ff.close()

    def test_search_baidu(self):
        self.ff.get("http://www.baidu.com")
        elem = self.ff.find_element_by_id('kw1')
        elem.send_keys("qq" + Keys.RETURN)
        #time.sleep(5)

        parentDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print parentDir

        try:
            self.ff.find_element_by_xpath("//a[contains(@href,'http://baike.baidu.com1')]")
        except NoSuchElementException:
            assert 0, "can't find baike"
            #self.ff.get_screenshot_as_file(parentDir+os.sep+'report'+os.sep+'dadd.png')


if __name__ =='__main__':
    unittest.main()
    print 'gwegwgwgwge= feww=ff=ewwe=f=wfwe='