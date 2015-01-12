__author__ = 'zhangchun'
# coding=utf-8
import unittest
from time import sleep

from framework.core import device_bak, the


#点击登录图标进入登录页面

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)


    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()

        sleep(2)
        self.driver.switch_to_alert()
        self.assertEqual('.UserInformationActivity',self.driver.current_activity)