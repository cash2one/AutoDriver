# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
import unittest
from framework.core import idriver_android

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.customer_robot()
        self.driver.login()

    def tearDown(self):
        pass

    def test_call_order(self):
        #写具体执行下订单操作
        current_activity = self.driver.current_activity
        #self.driver.find_id('bt_order').click()
        print('下单')



if __name__ == '__main__':
    unittest.main()