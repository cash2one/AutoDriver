# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        # self.driver.switch_to_home()
        # 关闭浏览器
        self.driver.close()

    #修改链接
    def test_update(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        uptx=self.driver.find_element_by_id('update').text
        self.assertTrue(u'修改' in uptx)
        self.driver.find_element_by_id('update').click()

