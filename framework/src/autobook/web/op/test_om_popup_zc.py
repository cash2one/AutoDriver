__author__ = 'Administrator'
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
        self.ff.implicitly_wait(10) #设置网页打开超时时间

        self.ff.maximize_window()
    def tearDown(self):
        self.ff.close()


    def test_2(self):
        self.ff.get("http://192.168.3.81/om/%E4%B8%AA%E4%BA%BA%E8%AE%BE%E7%BD%AE_%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF.html")
        self.ff.find_element_by_id('u71').click()

        try:
            alert = self.switch_to_alert()
            alert.accept()
        except:
            print 'no alerts display'


    def test_1(self):
        self.ff.get("http://192.168.3.81/om/%E4%B8%AA%E4%BA%BA%E8%AE%BE%E7%BD%AE_%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF.html")
        self.ff.find_element_by_id('u71').click()
        #self.ff.execute_script("alert('hihihi')")

        try:
            #self.switch_to_alert()
            about_text=self.ff.find_element_by_id("u85").text
            self.assertTrue(u'恭喜你！更新数据成功！'in about_text)

        finally:
            pass


if __name__ =='__main__':
    unittest.main()