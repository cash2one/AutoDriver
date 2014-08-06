# coding=utf-8
__author__ = 'Administrator'
import unittest
from time import sleep
from framework.core import gvar,device


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        self.driver = gvar.driver

    def tearDown(self):
        #self.driver.close_app()
        device.switchToHome(self,self.mainActivity)

    def test_text(self):
        sleep(15)
        self.mainActivity = self.driver.current_activity

        self.driver.find_element_by_name(u'聚乐会').click()

        sleep(10)
        self.driver.find_element_by_name(u'详情').click()

        sleep(1)

        # sleep(1)
        # self.driver.find_element_by_name(u'取消').click()
        # self.driver.keyevent(4)

