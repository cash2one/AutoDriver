# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

#查询成功

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

    def test_query(self):
        #查询客户下单的结果
        allOptions = self.driver.find_element_by_id('orderSource').find_elements_by_tag_name('option')
        for option in allOptions:
         if option.get_attribute('text')==u'客户下单':
           option.click()
         self.driver.find_element_by_id('query').click()

    def test_query1(self):
        #查询平台下单的结果
        opts=self.driver.find_element_by_id('orderSource').find_elements_by_tag_name('option')
        print opts
        for opt in opts:
            if opt.get_attribute('text')==u'平台下单':
                opt.click()

        self.driver.find_element_by_id('query').click()
        time.sleep(2)

    def test_query2(self):
        #查询全部订单（全部来源）的结果
        opts=self.driver.find_element_by_id('orderSource').find_elements_by_tag_name('option')
        print opts
        for opt in opts:
            if opt.get_attribute('text')==u'全部来源':
                opt.click()

        self.driver.find_element_by_id('query').click()
        time.sleep(2)

    def test_query3(self):
        #查询微信下单的结果
        opts=self.driver.find_element_by_id('orderSource').find_elements_by_tag_name('option')
        print opts
        for opt in opts:
            if opt.get_attribute('text')==u'微信下单':
                opt.click()

        # table=self.driver.find_element_by_id('table')
        # trs=table.find_elements_by_tag_name('tr')
        #
        # try:
        #    orderInfo_customer_name = trs.find_element_by_id('')>0
        #
        # except exceptions.NoSuchElementException:
        #     pass
        self.driver.find_element_by_id('query').click()
        time.sleep(2)

    def test_query4(self):
        #查询全部任务（订单来源默认）
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        print opts
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()

        self.driver.find_element_by_id('query').click()
        time.sleep(2)

    def test_query5(self):
        #查询默认待分配任务（订单来源默认）
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        print opts
        for opt in opts:
            if opt.get_attribute('text')==u'待分配任务':
                opt.click()

        self.driver.find_element_by_id('query').click()
        time.sleep(2)


    def test_query6(self):
        #查询我的任务（订单来源默认）
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        print opts
        for opt in opts:
            if opt.get_attribute('text')==u'我的任务':
                opt.click()

        self.driver.find_element_by_id('query').click()
        time.sleep(2)





if __name__ =='__main__':
    unittest.main()