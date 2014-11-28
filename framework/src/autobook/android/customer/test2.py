# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_call_server(self):
        print idriver_android.client()
        time.sleep(10)