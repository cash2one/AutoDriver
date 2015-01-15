# coding=utf-8
__author__ = 'guanghua_2011@126.com'

import time
import unittest
from framework.core import testcase

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.customer_robot()
        pass

    def tearDown(self):
        pass

    def test_call_order(self):
        #写具体执行下订单操作
        print u'我已经下了订单'

if __name__ == '__main__':
    unittest.main()