# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    #禁用提示
    def test_forbidden(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        self.driver.find_element_by_id('stop').click()
        self.driver.switch_to_alert()
        #弹出框标题内容
        xxtxt=self.driver.find_element_by_xpath(' /html/body/div[6]/div[1]/div[2]/em').text
        self.assertTrue(u'信息' in xxtxt)
        #弹出框提示内容
        jytxt=self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/span[2]').text
        self.assertTrue(u'确定禁用？' in jytxt)

    #禁用操作
    def test_forbidden_cancel(self):
        self.test_forbidden()
        #取消
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/span[2]/a[2]').click()
        time.sleep(5)

     #禁用操作
    def test_forbidden_confirm(self):
        self.test_forbidden()
        #确定
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/span[2]/a[1]').click()
        time.sleep(5)

