# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#点击详情中的预约保养，选择指定时间，点击确定，预约成功
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
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000004')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        sleep(5)
        self.driver.find_element_by_name (u'详情').click()
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        #进入预约保养界面
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #选择期望时间
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #预约成功后，保养预约按钮变为取消预约按钮
        sleep(3)
        text1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').text
        self.assertEqual(u'取消预约',text1)
