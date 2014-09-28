__author__ = 'zhangchun'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.maximize_window()

    def tearDown(self):
        self.ff.close()

    def test_4(self):
        self.ff.get("http://192.168.3.81/om/%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86_%E6%B7%BB%E5%8A%A0.html")
        self.ff.find_element_by_link_text(u"个人设置").click()
        time.sleep(2)
        try:
            self.assertTrue('http://192.168.3.81/om/%E4%B8%AA%E4%BA%BA%E8%AE%BE%E7%BD%AE_%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF.html' in self.ff.current_url)
            about_text=self.ff.find_element_by_id('u70_rtf').text
            self.assertTrue(u'个人信息' in about_text)
            self.ff.find_element_by_id('u73').clear()
            time.sleep(1)
            self.ff.find_element_by_id('u73').send_keys("13725156545")
            time.sleep(1)
            self.ff.find_element_by_id('u71').click()
            time.sleep(1)
            try:
                about_text=self.ff.find_element_by_id('u84_rtf').text
                self.assertTrue(u'操作结果' in about_text)
            except NoSuchElementException:
                print "not"
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'result'+os.sep+'geweg.png')
            pass

if __name__ =='__main__':
    unittest.main()