# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    查询司机信息明细
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()
    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    def test_driverDetails(self):
        '''
        查看司机信息明细
        :return:
        '''
        self.driver.find_ajax_id('orderInfo_driver_name')

        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #点击第一行的司机信息
        trs[1].find_element_by_id('orderInfo_driver_name').click()
        time.sleep(2)
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_title').text
        print text
        self.assertTrue(u'司机信息明细' in text,'msg')

    def test_closeWindow(self):
        '''
        关闭司机信息弹出框
        :return:
        '''
        self.driver.find_ajax_id('orderInfo_driver_name')

        table=self.driver.find_element_by_id('list')
        trs=table.find_elements_by_tag_name('tr')
        #点击第一行的司机信息
        trs[1].find_element_by_id('orderInfo_driver_name').click()
        time.sleep(1)

        #点击关闭按钮
        self.driver.find_element_by_link_text('关闭').click()
        time.sleep(2)
        isClose=True
        try:
            self.driver.find_element_by_id('xubox_main')
            isClose=False
        except self.driver.NoSuchElementException:
            isClose=True

        self.assertTrue(isClose,u'司机信息明细框没有被关闭')
        time.sleep(2)




