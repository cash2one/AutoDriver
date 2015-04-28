# coding=utf-8
__author__ = 'ggh'

import time
from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app()

    def tearDown(self):
        pass

    def test_StringValue(self):
        cal = self.driver.find_class('com.testing.pkg.Calculator')
        result = cal.getBoolResult(6, 3)
        self.assertEquals(result, True)

    def test_NumberValue(self):
        cal = self.driver.find_class('com.testing.pkg.Calculator')
        result = cal.getNumResult(3, 5)
        self.assertEquals(result, 9)


if __name__ == '__main__':
    unit.unittest.main()