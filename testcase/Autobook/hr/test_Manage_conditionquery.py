__author__ = 'gaoxu@pathbook.com.cn'
# coding=utf-8

import time
import unittest
from framework.core import idriver_web


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        #登录平台
        self.driver.login()

    def tearDown(self):
         #返回首页
        # self.driver.switch_to_home()
        time.sleep(5)
         #关闭浏览器
        self.driver.close()
    def initInputValue(self,driver_no,driver_name,driver_phone,driver_idnumber):
        #司机管理
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        #司机工号
        self.driver.find_element_by_id('driverInfo').click()
        self.driver.find_element_by_id('driverInfo').send_keys(driver_no)
        #司机姓名
        self.driver.find_element_by_id('driverInfo').click()
        self.driver.find_element_by_id('driverInfo').send_keys(driver_name)
        #司机电话
        self.driver.find_element_by_id('driverInfo').click()
        self.driver.find_element_by_id('driverInfo').send_keys(driver_phone)
        #司机身份证号
        self.driver.find_element_by_id('driverInfo').click()
        self.driver.find_element_by_id('driverInfo').send_keys(driver_idnumber)
        #点击查询按钮
        self.driver.find_element_by_id('query').click()

    #输入不存在的司机工号
    def test_value1(self):
        self.initInputValue('999999999','','','')
        txt = self.driver.find_element_by_class_name('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,'false')

    #输入不存在的司机姓名
    def test_value2(self):
        self.initInputValue('',u'张大小','','')
        txt = self.driver.find_element_by_class_name('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,'false')

    #输入不存在的司机电话
    def test_value3(self):
        self.initInputValue('','','12311012202','')
        txt = self.driver.find_element_by_class_name('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,'false')

    #输入不存在的身份证号码
    def test_value4(self):
        self.initInputValue('','','',u'61232111012230587X')
        txt = self.driver.find_element_by_class_name('norecords').text
        print txt
        self.assertTrue(u'没有符合条件的数据...' in txt ,'false')

    #输入正确的司机工号
    def test_correct_value1(self):
        self.initInputValue('14000','','','')
        txt = self.driver.find_element_by_id('list').text
        print txt

    #输入正确的司机姓名
    def test_correct_value2(self):
        self.initInputValue('',u'李雅文','','')
        txt = self.driver.find_element_by_id('list').text
        print txt

     #输入正确的电话
    def test_correct_value3(self):
        self.initInputValue('','','13122302705','')
        txt = self.driver.find_element_by_id('list').text
        print txt

    #输入正确的身份证号码
    def test_correct_value4(self):
        self.initInputValue('','','','612321198205061275')
        txt = self.driver.find_element_by_id('list').text
        print txt
    #文本框为空
    def test_correct_null(self):
        self.initInputValue('','','','')
        txt = self.driver.find_element_by_id('list').text
        print txt
        #司机状态
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts:
            if opt.get_attribute('value')=='0':
                opt.click()
        txt=self.driver.find_element_by_id('query').click()
        print txt