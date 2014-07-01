__author__ = 'zhangchun'
# coding=utf-8

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#from util.fileUtil import *

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        #self.ff.implicitly_wait(10) #设置网页打开超时时间

    def tearDown(self):
        self.ff.close()

    def test_search_baidu(self):
        self.ff.get("http://192.168.3.28/om/") #测试网页地址
        self.ff.find_element_by_id('u2').send_keys(u"张三" )#测试标签到的id
        self.ff.find_element_by_id('u3').send_keys("123456")#测试输入的内容
        self.ff.find_element_by_id('u4').click()
        #time.sleep(20) 睡眠20S

        try:
            self.assertTrue('http://192.168.3.28/om/%E9%A6%96%E9%A1%B5.html' in self.ff.current_url)
            about_text=self.ff.find_element_by_id('cache3').text
            self.assertTrue(u'个人设置' in about_text)
        finally:
            #self.ff.get_screenshot_as_file(parentDir()+os.sep+'report'+os.sep+'geweg.png')
            pass


if __name__ =='__main__':
    unittest.main()
    print 'gwegwgwgwge= feww=ff=ewwe=f=wfwe='