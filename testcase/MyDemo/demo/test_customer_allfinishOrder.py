# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        pass

    def test_print_f(self):
        slogan = self.driver.find_element_by_class_name('slogan').text

        self.assertTrue(u'您的爱车代驾首选' in slogan,'no content')
