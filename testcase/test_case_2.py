__author__ = 'Administrator'

from selenium import selenium
import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*mock", "http://localhost:4444")
        self.selenium.start()
        self.selenium.open("http://www.baidu.com")

    def tearDown(self):
        self.selenium.stop()

    def test_sum1(self):
        print 'case2_0...'

    def test_sum2(self):
        print 'case2_1...'

if __name__ =='__main__':
    unittest.main()