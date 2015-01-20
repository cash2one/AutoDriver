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

    #查询分页
    def test_logall(self):
        above=self.driver.find_element_by_link_text(u'日志查询')
        ActionChains(self.driver).move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        time.sleep(1)
        opts=self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option')
        for opt in opts:
            #判断text里面的内容等不等于客服专员
            if opt.get_attribute('text')=='20':  #获取对象属性
                opt.click()

            else:
                opt.get_attribute('text')==u'40'
                opt.click()




