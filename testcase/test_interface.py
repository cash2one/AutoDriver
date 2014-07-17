__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from util.files import *
from util import jsons
import json
from util import xls
from util import files
import json

class TestCase(unittest.TestCase):

    def setUp(self):
        filename=files.base_dir + os.sep + 'config' + os.sep+'autobook_app.xls'
        #tables = xls.Excel(filename).readByIndex(0,0)#.readByName(2, 'Sheet1')
        j=self.arrays= xls.Excel(filename).readTestCaseByConf()
        print xls.mergeGroup(j)

    def tearDown(self):
        pass

    def test_weather(self):
        pass
        # for a in self.arrays:
        #     if a[u'用例描述']!='':
        #         inf_value=jsons.find_value_by_url(a[u'用例描述'])
        #         wish = a[u'期望结果']
        #         num=int(a[u'用例编号'])
        #         #self.assertEqual(jsons.fromStr(wish),inf_value,'编号为['+str(num)+']的用例，与期望结果不一致')
        #         self.assertTrue(jsons.fromStr(wish)==inf_value,'testttt')
                # try:
                #     assert(jsons.fromStr(wish)==inf_value)
                # except AssertionError,msg:
                #     print msg
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
        #self.assertEqual(jsons.fromStr(a),jsons.find_value_by_url('http://www.weather.com.cn/data/sk/101020100.html'),'不相等')
        # try:
        #
        #     self.assertEqual('JC_RADAR_AZ9210_JB',ff,'fail')
        # finally:
        #     pass

    def getTestValue(self):
        filename=files.base_dir + os.sep + 'config' + os.sep+'autobook_cs.xls'


if __name__ =='__main__':
    unittest.main()