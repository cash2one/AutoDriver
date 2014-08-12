# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#点击登录，检查性别选择框
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.android()

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        sleep(5)
        self.mainActivity = self.driver.current_activity
