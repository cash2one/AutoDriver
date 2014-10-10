# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import android_ium,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = android_ium.Android()
        self.driver.login('idriver_driver')

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_my_info(self):
        idriver.changeWork(True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('iv_head').click()

        self.driver.switch_finish(current_activity)

        title_text = self.driver.find_id('tv_title_text').text
        self.assertTrue(u'个人中心' in title_text,'no')
        # self.driver.find_id('personal_list').find_tags('android.widget.LinearLayout')[0].click()
        # time.sleep(1)

        # self.driver.find_elements_by_id('cn.com.pathbook.idriver.driver:id/lv_order')
        # self.drivers.find_elements_by_accessibility_id('cn.com.pathbook.idriver.driver:id/lv_order')
        #
        # customer_name = device.findDynamicId('cn.com.pathbook.idriver.driver:id/tv_customer_name')
        #
        # self.driver.find_element_by_id('cn.com.pathbook.idriver.driver:id/iv_waiting')
        # self.driver.find

        #cn.com.pathbook.idriver.driver:id/tv_customer_name

        #cn.com.pathbook.idriver.driver:id/tb_work_state

