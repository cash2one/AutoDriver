__author__ = 'xhl'
# coding=utf-8
#hr_循环添加司机多选框测试lll
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.close()

    #查询（状态）
    def test_my_select(self):
         opts=self.driver.find_element_by_id('status').find_elements_by_tag_name('option')
         for opt in opts:

            if opt.get_attribute('text')==u'禁用':  #获取对象属性
                opt.click()
         self.driver.find_element_by_id('query').click()
         time.sleep(4)
         trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')

         if len(trs)>1:
            for i in (1,len(trs)-1):
                text=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[i].find_elements_by_tag_name('td')[6].text

                self.assertEqual(text,u"已禁用")
         else:
            pass
         time.sleep(4)