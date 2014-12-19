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
        #自动订单发送cmd
        driver_file = os.path.dirname(__file__).replace('customer', 'driver')
        script = os.path.join(driver_file, 'test_order_robot.py')

        print self.driver.auto_order(script)