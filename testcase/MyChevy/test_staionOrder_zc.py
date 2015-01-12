# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep

from framework.core import device_bak, the


#预约保养成功后，在服务站详情中显示取消预约按钮
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
        sleep(2)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000005')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').click()
        #选择指定位置

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[2].click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(2)
        #选择期望时间

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(3)
        #预约成功
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_station').click()
        self.driver.find_element_by_name (u'详情').click()
        txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').text
        self.assertEqual(u'取消预约',txt)
