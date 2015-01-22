# coding=utf-8
__author__ = 'xhl'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_monitoringRefresh(self):
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'客户监控').click()
        self.driver.find_id('query').click()



    def test_Drivermonitoring(self):
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')

        self.assertTrue(opts[0].text==u'全部')
        tuple=(u'全部',u'空闲',u'休息',u'服务中')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')
            print(type)
            if not type in tuple:
                isExist = False
                break
        self.assertTrue(isExist,'false')




