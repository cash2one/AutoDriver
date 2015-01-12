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
        self.driver.switch_to_home()
        time.sleep(5)
         #关闭浏览器
        # self.driver.close()

    def test_main_footer(self):
        tex=self.driver.find_element_by_id('main_footer').text
        self.assertTrue(u'途谱（上海）信息科技有限公司 |' in tex)
        print tex

    def test_helpInfo(self):
        tex=self.driver.find_element_by_id('_helpInfo').click()
        print tex

