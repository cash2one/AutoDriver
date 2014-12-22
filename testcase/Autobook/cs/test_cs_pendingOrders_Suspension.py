__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
#查询司机信息明细

import time
import unittest
from framework.core import idriver_web
from selenium.common import exceptions

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()
    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def test_supension_ok(self):
        time.sleep(2)
        #点击中止操作
        self.driver.find_element_by_id('closeOrder').click()
        time.sleep(2)

        #判断弹出窗口
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_dialog').text
        print text
        self.assertTrue(u'确定中止该订单？' in text,'msg')

        #点击确定按钮,关闭弹出的窗口
        button=self.driver.find_element_by_class_name('xubox_botton').text
        print button

        if u'确定' in  button:
            self.driver.find_element_by_class_name('xubox_botton').click()
        time.sleep(2)
        # d=self.driver.switch_to_alert()
        # d.accept()





