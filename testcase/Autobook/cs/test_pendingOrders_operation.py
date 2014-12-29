__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
#操作：我要处理、分配他人



import time
import unittest
from framework.core import idriver_web

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def initInputValue(self,order_No,customer_Info,driver_Info):

        self.driver.find_element_by_id('deal').click()

        button=self.driver.find_element_by_id('xubox_border6').find.elments_by_class_name('xubox_botton').text
        if u'确定' in  button:
            self.driver.find_element_by_class_name('xubox_botton').click()
        time.sleep(2)


