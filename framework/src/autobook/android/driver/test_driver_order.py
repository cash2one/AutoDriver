# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from framework.core import apps,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = apps.Android('android.idriver.driver2')
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_my_info(self):
        idriver.changeWork(True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('iv_head').click()

        self.driver.switch_finish(current_activity)

        title_text = self.driver.find_id('tv_title_text').text

        print self.driver.sql('select name from t_driver where id=40')
        self.assertTrue(u'个人中心' in title_text,'no')

        idriver.request_order(True)

