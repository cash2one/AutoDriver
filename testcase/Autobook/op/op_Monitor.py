# coding=utf-8
__author__ = 'xiaohengli@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_monitoringRefresh(self):
        '''
        1、列表实时更新在线司机的信息及状态，
        2、“开始监控”按钮变为“监控中...”
        1、列表停止更新在线司机的信息及状态
        2、“监控中...”按钮变为“开始监控”
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在客户监控上
        self.driver.find_element_by_link_text(u'司机监控').click()
        self.driver.find_id('isMonitor').click()


