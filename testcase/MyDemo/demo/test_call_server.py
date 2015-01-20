# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        pass

    def tearDown(self):
        pass


    def test_print_e(self):
        # winxin_code = self.driver.find_element_by_class_name('winxin_code').find_element_by_tag_name('p').text
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'关注微信公众' in u'关注微信', u'关注微信')

    def test_print_f(self):
        # winxin_code = self.driver.find_element_by_class_name('winxin_code').find_element_by_tag_name('p').text
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'关注微信公众' in u'关注微信', u'关注微信')