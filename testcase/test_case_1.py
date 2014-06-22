__author__ = 'Administrator'
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.implicitly_wait(10) #设置网页打开超时时间

    def tearDown(self):
        self.ff.close()

    def test_sum1(self):
        self.ff.get("http://www.baidu.com")
        assert u'百度' in self.ff.title

    def test_sum2(self):
        self.ff.get("http://www.baidu.com")
        elem = self.ff.find_element_by_id('kw1')
        elem.send_keys("qq" + Keys.RETURN)
        #time.sleep(5)
        try:
            self.ff.find_element_by_xpath("//a[contains(@href,'http://baike.baidu.com/view/15c')]")
            self.ff.save_screenshot('afww.jpg')
        except NoSuchElementException:
            assert 0, "can't find baike"


if __name__ =='__main__':
    unittest.main()