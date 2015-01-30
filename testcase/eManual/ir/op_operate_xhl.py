# coding=utf-8
__author__ = 'xhl'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    循环添加司机多选框测试lll
    '''
    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login('role_operation')

    def tearDown(self):
        #返回首页
        self.driver.close()


    def test_my_batch(self):
        self.driver.find_element_by_id('uploader').send_keys(u'你好啊')
        self.driver.find_element_by_id('query').click()





