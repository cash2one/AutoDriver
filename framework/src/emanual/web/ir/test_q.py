__author__ = 'Administrator'

# coding=utf-8

import unittest
from framework.core import emanual_web
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = emanual_web.firefox(__file__)
        self.driver.login('role_oper')

    def tearDown(self):

        self.driver.close()
    def test_my_batch(self):
        self.driver.find_element_by_id('uploader').send_keys(u'fd')
        self.driver.find_element_by_id('query').click()
