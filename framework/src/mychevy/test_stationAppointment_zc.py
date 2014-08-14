# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#点击取消预约按钮，成功取消
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

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
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000004')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(3)
        self.driver.find_element_by_name (u'详情').click()
        text1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').text
        el=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order')
        el.click()
        sleep(3)
        text2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').text
        print el.text
        print self.driver.current_activity
        self.assertEqual(text1,text2)