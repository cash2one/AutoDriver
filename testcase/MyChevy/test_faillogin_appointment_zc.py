# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#登录失败，点击保养预约维修，弹出登录用户不正确
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('zzzz')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000001')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').click()
         #登录失败
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        self.driver.switch_to_alert()
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_msg')
        txt=el.text
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').click()
        self.assertTrue(u'登录失败：用户信息不正确' in txt)
        self.assertFalse(el.is_displayed())

