# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    待处理订单页面：查看通讯记录、关闭通讯记录
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #查看通讯记录
    def test_communicationRecord(self):
        time.sleep(2)
        self.driver.find_ajax_id('communicationRecord')
        # #找到订单号，查看该通讯记录(遍例找订单号)
        # trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        # for i in range(1,len(trs)-1):
        #     tds=trs[i].find_elements_by_tag_name('td')
        #     if '15011515344163' in tds[2].text:
        #         try:
        #             tds[10].find_element_by_id('communicationRecord').click()
        #         except exceptions.NoSuchElementException:
        #             pass
        self.driver.find_element_by_id('orderNo').send_keys('15011515344163')
        #选择“全部任务”查询条件
        opts=self.driver.find_element_by_id('task').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'全部任务':
                opt.click()
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        tds=trs[1].find_elements_by_tag_name('td')
        if '15011515344163' in tds[1].text:
            try:
                tds[10].find_element_by_id('communicationRecord').click()
                time.sleep(2)
            except self.driver.NoSuchElementException:
                pass
        time.sleep(3)
        #点击通讯记录链接
        self.driver.find_element_by_id('communicationRecord').click()
        time.sleep(5)
        text=self.driver.find_element_by_class_name('xubox_title').text
        print text
        self.assertTrue('15011515344163' in text,u'没有找到该订单的订单号')
        # time.sleep(2)



    #关闭通讯记录
    def test_close_communicationRecord(self):

        self.driver.find_ajax_id('orderFlow')
        self.driver.find_element_by_id('communicationRecord').click()
        time.sleep(2)
        text=self.driver.find_element_by_class_name('xubox_title').text
        print text
        a=self.driver.switch_to_alert()
        # id=self.driver.find_element_by_id('xubox_border1')
        self.driver.find_element_by_class_name('xubox_close').click()
        time.sleep(2)
        isClose=True
        try:
            self.driver.find_element_by_id('xubox_main')
            isClose=False
        except self.driver.NoSuchElementException:
            isClose=True

        self.assertTrue(isClose,u'通讯记录内容没有被关闭')
        time.sleep(2)



     # isClose=False
     #    try:
     #        self.driver.find_element_by_id('xubox_main')
     #        isClose=True
     #    except exceptions.NoSuchElementException:
     #        isClose=False

