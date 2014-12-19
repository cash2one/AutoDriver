# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import os
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)

    def tearDown(self):
        pass

    def test_call_server(self):
        script = os.path.join(os.path.dirname(__file__), 'test_order_robot.py')
        print script
        print self.driver.auto_order(script)