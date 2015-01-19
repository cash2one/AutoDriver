# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        #self.driver = self.app(__file__)
        pass

    def tearDown(self):
        pass

    def test_print_a(self):
        self.assertTrue(u'您的爱车代驾首选' in '您的爱车','no content')

    def test_print_b(self):
        self.assertTrue(u'您的爱车代驾首选' in '您的爱车','no content')

    def test_print_c(self):
        #slogan = self.driver.find_element_by_class_name('slogan').text

        self.assertTrue(u'您的爱车代驾首选' in '您的爱车','no content')