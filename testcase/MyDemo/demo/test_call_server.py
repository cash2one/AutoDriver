# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

from drivers import *
from drivers import Autobook_cs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest


class TT(WebDriver):
    def __init__(self):
        firefox_profile = None
        firefox_binary = None
        capabilities = None
        proxy = None
        timeout = 30
        super(TT, self).__init__(firefox_profile, firefox_binary, timeout,
                                      capabilities, proxy)

    def action_chains(self):
        return ActionChains(self)#.move_to_element(ele).perform()


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = TT()
        pass

    def tearDown(self):
        pass

    def test_print_d(self):
        self.driver.get('http://www.oschina.net/')
        a=self.driver.find_element_by_link_text(u'开源中国')
        self.driver.action_chains().move_to_element(a).perform()


    def test_print_e(self):
        # winxin_code = self.driver.find_element_by_class_name('winxin_code').find_element_by_tag_name('p').text

        self.assertTrue(u'关注微信公众' in '关注微信', 'no content')

    def test_print_f(self):
        # winxin_code = self.driver.find_element_by_class_name('winxin_code').find_element_by_tag_name('p').text

        self.assertTrue(u'关注微信公众' in '关注微信', 'no content')