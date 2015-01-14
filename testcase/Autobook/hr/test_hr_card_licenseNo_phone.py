__author__ = 'lvfangying@pathbook.com.cn'
# coding=utf-8
#hr_循环验证用户名错误登录测试

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# from util.fileUtil import *
import os


class TestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()#打开火狐浏览器
       #浏览器最大化
        self.ff.maximize_window()

    def testValue(self):
        #打开网址路径
        self.ff.get("http://192.168.3.31/hr/")
        time.sleep(3)
        #清除文本框中已有的数据
        self.ff.find_element_by_id('username').clear()
        #在文本框中输入值
        self.ff.find_element_by_id('username').send_keys("rs1202")

        self.ff.find_element_by_id('password').clear()
        #在文本框中输入值
        self.ff.find_element_by_id('password').send_keys("1138051554")
        time.sleep(5)

    def test_card(self):
        self.testValue()
        self.ff.find_element_by_id('btn_add').click()
        driverVo_card_tx=self.ff.find_element_by_id('driverVo_card_tip').text
        self.assertTrue(u'身份证号不能为空.'in driverVo_card_tx)

    def test_card1(self,driver_card):
        self.testValue()
        self.ff.find_element_by_id('driverVo_card').send_keys(driver_card)


    def test_card_long(self):
        self.test_card1('4305231993020241403')
        # 身份证超长
    def test_card_special(self):
        self.test_card1('@#$$')
        # 身份证为特殊字符
    def test_card_j(self):
        self.test_card1(u'43052319921213434k')
        # 身份证最后一位为大小写字母
    def test_card_Non_capital_letters(self):
        self.test_card1(u'43052319921213434x')
        # 身份证最后一位为小写字母x
    def test_card_ture(self):
        self.test_card1('430523199302024140')
        # 正确的身份证号


    def test_licenseNo(self):
        self.testValue()
        self.ff.find_element_by_id("btn_add").click()
        test_licenseNo_tx=self.ff.find_element_by_id('detailVo_licenseNo_tip').text
        self.assertTrue(u'驾照档案编号不能为空.'in test_licenseNo_tx)


    def test_detailVo_licenseNo(self,detailVo_licenseNo):
        self.testValue()
        self.ff.find_element_by_id('detailVo_licenseNo').send_keys(detailVo_licenseNo)

    def test__licenseNo_null(self):
        self.test_detailVo_licenseNo('')
        # 驾照档案编号为空
    def test_licenseNo_long(self):
        self.test_detailVo_licenseNo('22222222222222222')
        # 驾照档案编号输入超长
    def test_licenseNo_special(self):
        self.test_detailVo_licenseNo('@#$$')
        # 驾照档案编号输入特殊字符
    def test_licenseNo_j(self):
        self.test_detailVo_licenseNo(u'ghk')
        # 驾照档案编号输入大小写字母
    def test_licenseNo_ture(self):
        self.test_detailVo_licenseNo('22522')
        # 输入正确的驾照档案编号



    def test_phone(self):
        self.testValue()
        self.ff.find_element_by_id('btn_add').click()
        test_phone_tx=self.ff.find_element_by_id('driverVo_phone_tip').text
        self.assertTrue(u'本人联系电话不能为空.'in test_phone_tx)


    def test_driverVo_phone(self,driverVo_phone):
        self.testValue()
        self.ff.find_element_by_id('driverVo_phone').send_keys(driverVo_phone)

    def test__phone_null(self):
        self.test_driverVo_phone('')
        # 本人联系电话为空
    def test_phone_long(self):
        self.test_driverVo_phone('181173515211')
        # 本人联系电话输入超长
    def test_phone_special(self):
        self.test_driverVo_phone('@#$$')
        # 本人联系电话输入特殊字符
    def test_phone_j(self):
        self.test_driverVo_phone(u'ghk')
        # 本人联系电话输入大小写字母
    def test_phone_ture(self):
        self.test_driverVo_phone('15618633412')
        # 输入正确的本人联系电话
