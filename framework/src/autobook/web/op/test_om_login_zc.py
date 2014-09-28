__author__ = 'zhangchun'
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from util.fileUtil import *
import os

class TestCase(unittest.TestCase):

    def setUp(self):
        self.ff = webdriver.Firefox()
        self.ff.get("http://192.168.3.81/om/")
        self.ff.maximize_window()

    def tearDown(self):
        self.ff.close()


    def initInputValue(self,user_name,pwd,img_code,pid,ptext):
        self.ff.find_element_by_id('u4').clear()
        self.ff.find_element_by_id('u4').send_keys(user_name)

        self.ff.find_element_by_id('u5').clear()
        self.ff.find_element_by_id('u5').send_keys(pwd)

        self.ff.find_element_by_id('u8').clear()
        self.ff.find_element_by_id('u8').send_keys(img_code)
        time.sleep(3)  # 睡眠3S

        self.ff.find_element_by_id('u6').click()
        try:
              about_text=self.ff.find_element_by_id(pid).text
              self.assertTrue(ptext in about_text)
        finally:
            pass

    def test_login_1(self):
        self.initInputValue(' ',' ','','u60',u'请输入用户名')

    def test_login_2(self):
        self.initInputValue(u'张三',' ','','u61',u'请输入密码')

    def test_login_3(self):
        self.initInputValue(u'张￥三#',' ','','u63',u'用户名格式有误')

    def test_login_4(self):
        self.initInputValue(u'张三','123456 ','','u63',u'密码不正确')

    def test_login_5(self):
        self.initInputValue(u'张三','1#11@1','','u63',u'密码格式有误')

    def test_login_6(self):
        self.initInputValue(u'张三','1111','','u63',u'请输入校验码')

    def test_login_7(self):
        self.initInputValue(u'张三','1111','erwQ','u63',u'校验码错误')

    def test_login_8(self):
        self.initInputValue(u'张三','1111','ffff','u63',u'登录成功')

    def test_login_9(self):
        self.initInputValue(u' 张三 ','  1111 ',' ffff ','u63',u'登录成功')

    def test_login_10(self):
        self.initInputValue(u' 张四 ','2222','ffff','u63',u'用户名不存在')


if __name__ =='__main__':
    unittest.main()
    print 'gwegwgwgwge= feww=ff=ewwe=f=wfwe='