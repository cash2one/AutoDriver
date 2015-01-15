# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
import unittest
from selenium.webdriver.common.keys import Keys
from framework.core import testcase

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()
    #页码
    def test_pager(self):

        #点击下一页
        self.driver.find_element_by_id('next_pager').click()
        time.sleep(2)
        #点击最后一页
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(2)
        #点击上一页
        self.driver.find_element_by_id('prev_pager').click()
        time.sleep(2)
        #点击第一页
        self.driver.find_element_by_id('first_pager').click()
        time.sleep(2)
        #输入页码
        input = self.driver.find_element_by_class_name('ui-pg-input')
        input.clear()
        input.send_keys('13')
        input.send_keys(Keys.ENTER)#输入回车键
        time.sleep(2)
        #输入第一页，并跳转
        input = self.driver.find_element_by_class_name('ui-pg-input')
        input.clear()
        input.send_keys('1')
        input.send_keys(Keys.ENTER)#输入回车键
        time.sleep(2)
        #选择每页10行
        self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option')[0].click()
        time.sleep(1)
        #选择每页20行
        self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option')[1].click()
        time.sleep(1)
        #选择每页40行
        self.driver.find_element_by_class_name('ui-pg-selbox').find_elements_by_tag_name('option')[2].click()
        time.sleep(1)



if __name__ =='__main__':
    unittest.main()



