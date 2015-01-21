# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_logType(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()

        opts=self.driver.find_id('logType').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'日志类型')

        tuple=(u'日志类型',u'用户日志',u'APP日志',u'接口日志',u'系统日志')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break

        self.assertTrue(isExist,'false')
        #查看日志类型下拉框中的选项


    def test_logLevel(self):
        above=self.driver.find_element_by_link_text(u'系统管理')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_link_text(u'系统日志').click()

        opts=self.driver.find_id('logLevel').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'日志级别')

        tuple=(u'日志级别',u'告警',u'信息',u'错误')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')

            if not type in tuple:
                isExist = False
                break

        self.assertTrue(isExist,'false')
        #查看日志类型下拉框中的选项
