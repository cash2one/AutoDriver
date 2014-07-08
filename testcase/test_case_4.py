__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.files import *
from util import parseJson
import json
from util import excel
from util import files

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_weather(self):
        filename=files.base_dir + os.sep + 'config' + os.sep+'autobook_hr.xls'
        tables = excel.Excel(filename).readByName(2, 'Sheet1')
        print tables
        # for row in tables:
        #     print row
        #print w.assertResult('city')
        #
        #webj=wi.find_value_by_url('http://www.weather.com.cn/data/sk/101020100.html')
        #jn = parseJson.fromStr(a)
        #print parseJson.find_value_by_key(jn, 'cityid')


        #self.assertEqual('JC_RADAR_AZ9210_JB',ff,'gwegwgwgwegwgwegwe')
        #print wi.strToJson(a)
        #u'\u4e5f\u6709'.encode('utf8')
        #self.assertEqual(parseJson.fromStr(a),parseJson.find_value_by_url('http://www.weather.com.cn/data/sk/101020100.html'),'不相等')
        # try:
        #
        #     self.assertEqual('JC_RADAR_AZ9210_JB',ff,'fail')
        # finally:
        #     pass


if __name__ =='__main__':
    unittest.main()