# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

        pass

    def tearDown(self):
        pass


    def test_print_oschina(self):
        self.driver.get('http://www.oschina.net')
        aa= self.driver.find_id('ProjectNews').find_class('TodayNewsTop1').find_tag('h2').text
        self.assertTrue(aa in 'dddd')

    def test_print_f(self):
        self.driver.get('http://www.cadillac.com.cn/ats_parameter.html')
        print self.driver.find_id('ATS').text