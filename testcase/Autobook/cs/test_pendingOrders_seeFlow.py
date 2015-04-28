# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    待处理订单页面：查看流程、关闭流程
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()
        self.verificationErrors = []


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_seeFlow(self):
        '''
        #查看订单流程
        :return:
        '''
        self.driver.find_ajax_id('orderFlow')
        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #点击第一行的“订单流程”
        trs[1].find_id('orderFlow').click()
        time.sleep(1)
        text=self.driver.find_id('gview_list2').find_class('ui-jqgrid-titlebar').text
        print text
        self.assertTrue(u'订单流程' in text,u'订单流程提示框不正确或不存在' )



    def test_seeFlow_close(self):
        '''
        #关闭订单流程
        :return:
        '''
        self.driver.find_ajax_id('orderFlow')
        table=self.driver.find_id('list')
        trs=table.find_tags('tr')
        #点击第一行的“订单流程”
        trs[1].find_id('orderFlow').click()
        time.sleep(2)
        # self.driver.switch_to_window()
        # aalhandles=self.driver.window_handles#获取所有窗口句柄
        # for handle in aalhandles:#在所有窗口中查找弹出窗口
        #     if handle!=nowhandle:
        #         self.driver.switch_to_window(handle)#这两步是在弹出窗口中进行的操作，证明我们确实进入了
        # self.driver.find_class('xubox_close').click()
        # time.sleep(2)
        # self.assertEqual([], self.verificationErrors)

        self.driver.find_class('xubox_close').click()
        isClose=True
        try:
            self.driver.find_id('gview_list2')
            isClose=False
        except self.driver.NoSuchElementException:
            isClose=True

        self.assertTrue(isClose,u'订单流程弹出框没有被关闭')
