# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#输入不存在的用户登录后，弹出提示框
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver =the.android

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep(2)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_cancel').click()
        #print(self.driver.current_activity)
        self.assertEqual('.MainActivity',self.driver.current_activity)
