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
         #鼠标悬停在客户监控上
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



    def test_DrivermonitoringAll(self):
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        time.sleep(3)
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'空闲':
                opt.click()
                self.assertTrue(opt.is_selected())
            elif opt.get_attribute('text')==u'全部':
                opt.click()
                self.assertTrue(opt.is_selected())

            elif opt.get_attribute('text')==u'休息':
                opt.click()
                self.assertTrue(opt.is_selected())

            elif opt.get_attribute('text')==u'服务中':
                opt.click()
                self.assertTrue(opt.is_selected())
            elif opt.get_attribute('text')==u'全部':
                opt.click()
                self.assertTrue(opt.is_selected())

    def test_Drivermonitoringselect(self):
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        #输入内容正常显示在文本框中
        self.driver.find_element_by_id('driverInfo').send_keys(u'小米')
        test=self.driver.find_element_by_id('driverInfo').text
        self.assertEqual(test,u'小米',u'没有进入对应页面')






