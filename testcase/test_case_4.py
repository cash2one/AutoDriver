__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.fileUtil import *
from util import parseJson
import json

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_weather(self):
        #print w.assertResult('city')
        a='{"weatherinfo":{"city":"上海","cityid":"101020100","temp":"26","WD":"东北风","WS":"1级","SD":"79%","WSE":"1","time":"17:50","isRadar":"1","Radar":"JC_RADAR_AZ9210_JB"}}'

        #webj=wi.find_value_by_url('http://www.weather.com.cn/data/sk/101020100.html')
        #jn = parseJson.fromStr(a)
        #print parseJson.find_value_by_key(jn, 'cityid')


        #self.assertEqual('JC_RADAR_AZ9210_JB',ff,'gwegwgwgwegwgwegwe')
        #print wi.strToJson(a)
        #u'\u4e5f\u6709'.encode('utf8')
        self.assertEqual(parseJson.fromStr(a),parseJson.find_value_by_url('http://www.weather.com.cn/data/sk/101020100.html'),'不相等')
        # try:
        #
        #     self.assertEqual('JC_RADAR_AZ9210_JB',ff,'fail')
        # finally:
        #     pass


if __name__ =='__main__':
    unittest.main()