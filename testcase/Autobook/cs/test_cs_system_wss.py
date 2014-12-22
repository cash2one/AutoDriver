__author__ = 'Administrator'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.url='http://192.168.3.112/cs/%E5%B9%B3%E5%8F%B0%E6%97%A5%E5%BF%97.html'
        self.ff.maximize_window()
        time.sleep(1)
        self.log_list=[]


    def tearDown(self):
        self.ff.quit()
        #self.log_list

    # def test_system_journal_level(self):
    #     self.ff.get(self.url)
    #     time.sleep(20)
        # opts=self.ff.find_element_by_id('u119').find_elements_by_tag_name('option')
        # for opt in opts:
        #     if opt.get_attribute('value')==u'日志级别':
        #         opt.click()
        # self.ff.find_element_by_id('u120').send_keys(u'普通')
        # time.sleep(1)
        # self.ff.find_element_by_id('u121').click()


    def test_system_journal_content(self):
        self.ff.get(self.url)
        #time.sleep(20)
        list=[]
        opts=self.ff.find_element_by_id('u119').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('value')==u'日志内容':
                list.append(opt)

        self.assertTrue(len(list)>0)



       # for inp in inps:
           # inp= self.ff.find_element_by_id('u119').find_elements_by_tag_name('input')[1]
        #    if inp.get_attribute('value')==u'日志内容':
        #         inp.click()
        # self.ff.find_element_by_id('u120').send_keys(u'订单队列已满')
        # time.sleep(1)
        # self.ff.find_element_by_id('u121').click()
        # try:
        #     box=self.ff.find_element_by_id('u119').find_elements_by_name(inp)
        #     self.assertEqual(u'日志内容', box.text,'')
            #self.assertSelected(u'日志内容' in box)
        # finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'result'+os.sep+'geweg.png')
            # pass


if __name__ =='__main__':
    unittest.main()