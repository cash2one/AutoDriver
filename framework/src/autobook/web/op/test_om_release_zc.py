__author__ = 'zhangchun'
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from util.fileUtil import *
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.get("http://192.168.3.81/om/%E9%A6%96%E9%A1%B5.html")
        # self.ff.implicitly_wait(10) #设置网页打开超时时间
        self.ff.maximize_window()

    def tearDown(self):
        self.ff.close()

    def initInputValue(self,title,content):
        self.ff.find_element_by_id('u124').clear()
        self.ff.find_element_by_id('u124').send_keys(title)

        self.ff.find_element_by_id('u127').clear()
        self.ff.find_element_by_id('u127').send_keys(content)
        time.sleep(3)  # 睡眠3S
        self.ff.find_element_by_id('u131').click()
        time.sleep(3)  # 睡眠3S
        self.ff.find_element_by_id('u161').click()

        try:
            self.assertTrue("http://192.168.3.81/om/%E9%A6%96%E9%A1%B5.html" in self.ff.current_url)
        finally:
            pass

    def test_release_1(self):
        self.initInputValue('','')
    def test_release_2(self):
        self.initInputValue('gsdg','')
    def test_release_3(self):
        self.initInputValue(u'维护管理维护管理维护管理维护管理维护管理维护管理','')
    def test_release_4(self):
        self.initInputValue(u'维护管理',u'飞机的关键是规范乐扣')
    def test_release_5(self):
        self.initInputValue('',u'飞机的关键是规范乐扣')
    def test_release_6(self):
        self.initInputValue(u' 维护 管理',u' 飞机的关键 是规范乐扣')

if __name__ == '__main__':
    unittest.main()