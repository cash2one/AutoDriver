# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import os
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer()

    def tearDown(self):
        pass

    def test_call_server(self):

        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        print self.driver.auto_order(PATH('./test_order_robot.py'))