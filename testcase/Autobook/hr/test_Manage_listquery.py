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


    #默认的条件查询
    def test_defaul(self):
        #司机管理
         self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        #点击查询按钮
         self.driver.find_element_by_id('query').click()
         pagetx=self.driver.find_element_by_id('sp_1_pager').text
         print pagetx
         txt=self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div/table').text
         print txt

    #一个条件，选择正确的条件查询
    def test_one_bxcorrect(self):
        #司机管理
         self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
          #司机工号
         self.driver.find_element_by_id('driverInfo').click()
         self.driver.find_element_by_id('driverInfo').send_keys('')
         #司机状态
         opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
         time.sleep(1)
         for opt in opts:
            if opt.get_attribute('value')=='0':
                opt.click()
         self.driver.find_element_by_id('query').click()
        #打印查询内容
         txt=self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div/table').text
         print txt

    #两个正确条件，选择正确的条件查询
    def test_two_correct(self):
        #司机管理
         self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
          #司机工号
         self.driver.find_element_by_id('driverInfo').click()
         self.driver.find_element_by_id('driverInfo').send_keys('14000')
         #司机状态
         opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
         time.sleep(1)
         for opt in opts:
            if opt.get_attribute('value')=='0':
                opt.click()
         self.driver.find_element_by_id('query').click()
         txt=self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div/table').text
         print txt

    #两个正确条件，文本错误条件查询
    def test_one_txerror(self):
        #司机管理
         self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
          #司机工号
         self.driver.find_element_by_id('driverInfo').click()
         self.driver.find_element_by_id('driverInfo').send_keys('12345678999')
         #司机状态
         opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
         time.sleep(1)
         for opt in opts:
            if opt.get_attribute('value')=='0':
                opt.click()
         self.driver.find_element_by_id('query').click()
         txt=self.driver.find_element_by_class_name('norecords').text
         print txt
         self.assertTrue(u'没有符合条件的数据...' in txt ,'false')


    #两个正确条件，下拉错误条件查询
    def test_one_boxerror(self):
        #司机管理
         self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
          #司机工号
         self.driver.find_element_by_id('driverInfo').click()
         self.driver.find_element_by_id('driverInfo').send_keys('14000')
         #司机状态
         opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
         time.sleep(1)
         for opt in opts:
            if opt.get_attribute('value')=='5':
                opt.click()
         self.driver.find_element_by_id('query').click()
         txt=self.driver.find_element_by_class_name('norecords').text
         print txt
         self.assertTrue(u'没有符合条件的数据...' in txt ,'false')
