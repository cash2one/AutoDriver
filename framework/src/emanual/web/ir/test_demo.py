__author__ = 'wangshanshan'
# coding=utf-8

import unittest
from framework.core import emanual_web
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = emanual_web.firefox(__file__)
        self.driver.login()


    def tearDown(self):
        self.driver.switch_to_home()


    def test_my_reset(self):
        # td=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[7]
        # td.find_elements_by_link_text(u'启用')[1].click()
        #
        # self.driver.switch_to_alert()
        # time.sleep(4)
        print self.driver.find_id('myNes').text
        self.driver.find_id('myNes').click()
        print self.driver.find_id('welcome').text






