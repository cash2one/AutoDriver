# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device_bak
from time import sleep
#查看未登录时是否有感叹号
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver =the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_notify')
        self.assertTrue(el.is_enabled())#感叹号存在