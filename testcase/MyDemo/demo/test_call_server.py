# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

from drivers import *

class TestCase(unit.TestCase):
    '''
    tetsetsetttee
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        pass

    def tearDown(self):
        pass


    def test_print_oschina(self):
        '''
        fewgweg  wwged eg
        :return:
        '''
        self.driver.get('http://www.oschina.net')
        aa= self.driver.find_id('ProjectNews').find_class('TodayNewsTop1').find_tag('h2').text
        self.assertTrue(aa in 'dddd','gwgwegegwewweg')

    def test_print_f(self):
        # winxin_code = self.driver.find_element_by_class_name('winxin_code').find_element_by_tag_name('p').text
        self.driver.get('http://www.baidu.com')
        self.assertTrue(u'关注微信公众' in u'关注微信', u'关注微信')