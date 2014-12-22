__author__ = 'wangshanshan'
# coding=utf-8

import unittest
from framework.core import emanual_web

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver=emanual_web.firefox(__file__)
        self.driver.login()


    def tearDown(self):
        self.driver.switch_to_home()

    def test_list(self):
        print self.driver.find_element_by_id('welcome').text


    def test_next(self):
        self.driver.find_element_by_id('myNes').click()
        self.driver.implicitly_wait(30)
        print self.driver.find_element_by_id('realName').text

    def test_qq(self):
        self.driver.get('http://www.qq.com')





