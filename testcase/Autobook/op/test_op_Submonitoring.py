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

    def test_Subplatform(self):
        '''
       下拉框中显示：默认、运行中、宕机、异常、未启动
        :return:
        '''
        li=self.driver.find_id('main_menu').find_tags('li')[1]
        above=li.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在子平台监控上
        li.find_element_by_link_text(u'子平台监控').click()
        opts=self.driver.find_element_by_id('state').find_tags('option')
        self.assertTrue(opts[0].text==u'默认')
        tuple=(u'默认',u'运行中',u'宕机',u'异常',u'未启动')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')
            print(type)
            if not type in tuple:
                isExist = False
                break
        self.assertTrue(isExist,'false')