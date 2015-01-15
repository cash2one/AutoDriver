# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
import unittest
from framework.core import testcase
from selenium.common import exceptions

class TestCase(unittest.TestCase):
    '''
    导出文件
    '''

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_export_open(self):
        self.driver.find_element_by_id('export').click()
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_dialog').text
        self.assertTrue(u'确定导出？' in text,'msg')
        time.sleep(2)
        self.driver.find_element_by_link_text('确定').click()
        time.sleep(10)
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_dialog').text
        self.assertTrue(u'确定导出？' in text,'msg')
