# coding=utf-8
__author__ = 'zhangchun'

from time import sleep
from drivers import *

#点击预约保养弹出提示框
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        # sleep(3)
        # self.driver.switch_to_alert()
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        # self.driver.switch_to_alert()
        # self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_location').click()
        sleep(5)
        txt1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').text
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').click()
        #选择指定位置

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[4].click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(2)
        #选择期望时间

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok')
        sleep(3)
        self.driver.switch_to_home()

        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_notify_detail').click()
        sleep(3)
        txt2=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_name').text
        txt=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_cancel').text

        self.assertEqual(u'取消预约',txt)
        self.assertEqual(txt1,txt2)
