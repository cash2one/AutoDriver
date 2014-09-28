__author__ = 'Administrator'
# coding=utf-8

import unittest

from framework.core import testcase

class TestCase(testcase.AndroidTestCase):

    def setUp(self):
        pass
        #self.ff = webdriver.Firefox()
        #self.ff.implicitly_wait(10) #设置网页打开超时时间

    def tearDown(self):
        pass

    def test_aa(self):
        print 'bbb'


if __name__ =='__main__':
    unittest.main()