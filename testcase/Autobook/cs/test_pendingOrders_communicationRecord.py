# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'





import time
import unittest
from framework.core import testcase
from selenium.common import exceptions

class TestCase(unittest.TestCase):
    '''
    待处理订单页面：查看通讯记录、关闭通讯记录
    '''

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #查看通讯记录
    def test_communicationRecord(self):
        self.driver.find_ajax_id('communicationRecord')
        #找到订单号，查看该通讯记录
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        for i in range(1,len(trs)-1):
            tds=trs[i].find_elements_by_tag_name('td')
            if '15011513577860' in tds[2].text:
                try:
                    tds[10].find_element_by_id('communicationRecord').click()
                except exceptions.NoSuchElementException:
                    pass

        #点击通讯记录链接
        self.driver.find_element_by_id('communicationRecord').click()
        text=self.driver.find_element_by_class_name('xubox_title').text
        print text

        # try:
        #     self.driver.find_element_by_id('communicationRecord').click()
        # except exceptions.NoSuchElementException:
        #     pass



        time.sleep(2)



    #关闭通讯记录
    def test_close_communicationRecord(self):

        self.driver.find_ajax_id('orderFlow')
        self.driver.find_element_by_id('communicationRecord').click()
        time.sleep(2)
        text=self.driver.find_element_by_class_name('xubox_title').text
        print text

        # id=self.driver.find_element_by_id('xubox_border1')
        self.driver.find_element_by_class_name('xubox_close').click()
        time.sleep(2)
        #self.driver.find_element.getText()
        #self.assertFalse()


