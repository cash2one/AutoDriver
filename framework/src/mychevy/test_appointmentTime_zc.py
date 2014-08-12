# coding=utf-8
__author__ = 'zhangchun'
import unittest
from framework.core import the,device
from time import sleep
#查看时间控件
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
        sleep(3)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        els=self.driver.find_elements_by_class_name('android.widget.ImageButton')
        els[0].click()
        els[1].click()
        els[2].click()
        els[3].click()
        els[4].click()
        els[5].click()
        els[6].click()
        els[7].click()
        els[8].click()
        els[9].click()
