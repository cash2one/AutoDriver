# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()


    def tearDown(self):
        pass

    def test_call_order(self):
        #写具体执行下订单操作
        print u'我已经下了订单'

if __name__ == '__main__':
    unittest.main()