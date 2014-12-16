__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
#创建订单



import time
import unittest
from framework.core import idriver_web
from selenium.webdriver.common.action_chains import ActionChains
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
                # above=self.driver.find_element_by_id('main_menu').click()
                ActionChains(self.driver).move_to_element(u'订单管理').perform()
                time.sleep(3)


