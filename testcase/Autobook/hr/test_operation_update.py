# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    #修改链接
    def test_update(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        self.driver.find_element_by_id('update').click()
