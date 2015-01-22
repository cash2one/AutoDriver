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

    def test_logall(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        time.sleep(1)
<<<<<<< Updated upstream
        opts=self.driver.find_class('ui-pg-selbox').find_tags('option')
=======
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        opts=self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option')
>>>>>>> Stashed changes
        for opt in opts:
            #判断text里面的内容等不等于客服专员
            if opt.get_attribute('text')=='10':  #获取对象属性
                opt.click()
                self.assertTrue(len(trs)=='11')
                time.sleep(1)

            elif opt.get_attribute('text')=='20':
                opt.click()
                time.sleep(1)
                self.assertTrue(len(trs)=='21')
            elif opt.get_attribute('text')=='40':
                opt.click()
                time.sleep(1)
                self.assertTrue(len(trs)=='41')




