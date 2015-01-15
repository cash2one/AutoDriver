# coding=utf-8
__author__ = 'xhl'


import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_logParameter(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        self.driver.find_element_by_id('params').send_keys(u'aaaaa')
        self.driver.find_element_by_id('query').click()
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        print len(trs)
        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)-1):
                #找到td
                text=trs[i].find_elements_by_tag_name('td')[6].text
                #判断是不是td里面的接口名称是不是driverService.dealOrder
                print text,i
                tuple=u'cancelType=1&orderNo=15011315092036&memo=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&requestId=14000513261766449233646&event=7&tokenNo=140005F4EFFC4E8A1D40FE850D85181D1CBC14'
                self.assertTure('aaaaa' in text)
        else:
            text=self.driver.find_element_by_class_name('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


