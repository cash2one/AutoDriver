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
        # self.driver.close()
    #禁用提示
    def test_forbidden(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        self.driver.find_element_by_id('start').click()
        self.driver.switch_to_alert()
        #弹出框标题内容
        xxtxt=self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/em').text
        self.assertTrue(u'信息' in xxtxt)
        #弹出框提示内容
        jytxt=self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/span[2]').text
        self.assertTrue(u'确定启用？' in jytxt)

    #启用操作
    def test_forbidden_cancel(self):
        self.test_forbidden()
       #取消
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/span[2]/a[2]').click()
        time.sleep(5)

     #启用操作
    def test_forbidden_confirm(self):
        self.test_forbidden()
        #确定
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/span[2]/a[1]').click()
        time.sleep(5)
