__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.fileUtil import *
from core import wi

class TestCase(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_weather(self):
        w = wi.WebInterface('http://www.weather.com.cn/data/sk/101020100.html')
        print w.assertResult('city')


if __name__ =='__main__':
    unittest.main()