__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
#查询失败



import time
import unittest
from framework.core import idriver_web
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def test_orderSuccess(self):

        menu=self.driver.find_element_by_id('main_menu').text
        print menu

        for i in range(len(menu)-1):
            if menu[i]==u'订单管理':
                self.driver.find_element_by_id('main_menu').click()
                time.sleep(3)

