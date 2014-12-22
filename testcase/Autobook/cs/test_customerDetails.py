__author__ = 'wangshanshan@pathbook.com.cn'
# coding=utf-8
#查询客户信息明细

import time
import unittest
from framework.core import idriver_web
from selenium.common import exceptions

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()
    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def test_customerDetails(self):
        self.driver.wait_find_id('orderInfo_customer_name')

        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #点击第一行的客户信息
        orderInfo_customer_name = trs[1].find_element_by_id('orderInfo_customer_name').click()
        time.sleep(2)
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_title').text
        print text
        self.assertTrue(u'客户信息明细' in text,'msg')

        # for tr in trs:
        #     tr.find_element_by_id('orderInfo_customer_name')

    def test_closeWindow(self):
        self.driver.wait_find_id('orderInfo_customer_name')

        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #点击第一行的客户信息
        orderInfo_customer_name = trs[1].find_element_by_id('orderInfo_customer_name').click()
        #点击关闭按钮(关闭客户信息明细窗口)
        self.driver.find_element_by_link_text('关闭').click()
        time.sleep(2)


if __name__ =='__main__':
    unittest.main()
