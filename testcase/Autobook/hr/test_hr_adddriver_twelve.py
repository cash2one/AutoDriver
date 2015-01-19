# coding=utf-8
__author__ = 'lvfangying@pathbook.com.cn'

#hr_循环验证用户名错误登录测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# from util.fileUtil import *
import os
from framework.core import testcase

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = testcase.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()


    def test_detailVo_licenseNum(self):
        self.driver.find_element_by_id('btn_add').click()
        test_licenseNum_tx=self.driver.find_element_by_id('detailVo_licenseNum_tip').text
        self.assertTrue(u'驾驶证号码不能为空.'in test_licenseNum_tx)

    def  test_licenseNum1(self,detailVo_licenseNum):
        self.driver.find_element_by_id('detailVo_licenseNum').send_keys(detailVo_licenseNum)

    def test__licenseNum_null(self):
        self.test_licenseNum1('')
        # 驾驶证号码为空
    def test_licenseNum_long(self):
        self.test_licenseNum1('4305231993020214230')
        # 驾驶证号码输入超长
    def test_licenseNum_special(self):
        self.test_licenseNum1('@#$$')
        # 驾驶证号码输入特殊字符
    def test_licenseNum_j(self):
        self.test_licenseNum1(u'43052319930202414k')
        # 驾驶证号码输入大小写字母
    def test_licenseNum_ture(self):
        self.test_licenseNum1('430523199302024140')
        # 输入正确的驾驶证号码







