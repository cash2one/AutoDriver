__author__ = 'zhangchun'
# coding=utf-8
import unittest

from framework.core import device_bak
from framework.data import the


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)


    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity

        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()
        self.driver.switch_to_alert()#获取弹出框
        #print(self.driver.current_activity)
        self.assertEqual('.NewPartyActivity',self.driver.current_activity)
