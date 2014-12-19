# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
import os
import unittest
from framework.core import idriver_android

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()
        pass

    def test_my_info(self):
        self.driver.change_status(True)
        self.driver.auto_order(PATH('../customer_robot/test_order_robot.py'))






if __name__ == '__main__':
    unittest.main()