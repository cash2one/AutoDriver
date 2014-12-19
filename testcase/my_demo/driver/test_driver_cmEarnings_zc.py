# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import sys
import time
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_print_f(self):
        result = __file__ + ':testcase'
        time.sleep(1)
        #self.assertTrue(False,result)
        print __file__,time.strftime("%H:%M:%S")
