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
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000001')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(3)
        self.driver.switch_to_alert()
        txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_msg').text
        #print txt
        self.assertTrue(u'登录失败：用户信息不正确'in txt)