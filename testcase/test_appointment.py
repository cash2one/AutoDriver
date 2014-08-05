# coding=utf-8
__author__ = 'Administrator'
import unittest
from time import sleep
from framework.core import gvar


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        self.driver = gvar.driver

    def tearDown(self):
        self.driver.close_app()

    def test_text(self):
        sleep(15)

        print self.driver.current_activity
        print self.driver.current_context

        self.driver.switch_to.context(None)
        self.driver.find_element_by_name(u'保养预约维修').click()
        sleep(2)
        self.driver.find_element_by_name(u'确定').click()