# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import app,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = app.Android()
        self.driver.login('idriver_driver')

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def my_info(self,):
        idriver.changeWork(True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('rb_order').click()
        self.driver.switch_finish(current_activity)

        self.driver.find_id('personal_list_text').click()
        self.driver.switch_finish(current_activity)
        self.assertTrue('<bound method Android.current_activity of <framework.core.extend.Android object at 0x01FE1190>>',self.driver.current_activity)


    def test_my_name(self):
        self.my_info()
        els=idriver.find_data('select name from t_driver where id =67')
        name=self.driver.find_id('text_name').text
        self.assertTrue(els,name)
