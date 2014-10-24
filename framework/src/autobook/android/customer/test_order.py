# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.Android('idriver.android.customer')
        idriver.start_customer(self.driver)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_my_info(self):
        #self.driver.find_id('rb_order').click()
        #time.sleep(1)

        self.driver.find_id('ll_title').find_elements_by_class_name('android.widget.Button')[1].click()

        # self.driver.find_id('person_two').click()
        # self.driver.find_id('tv_phone').send_keys(idriver.get_contact_phone())
        # self.driver.find_id('bt_order').click()

        time.sleep(1)
        print self.driver.current_activity


        #print self.driver.sql('select name from t_driver where id=40')

        #idriver.request_order(True)

