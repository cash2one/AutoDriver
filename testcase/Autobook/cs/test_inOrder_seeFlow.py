# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_inOrder_seeFlow(self):
        '''
        查看进行中订单中的订单流程（默认选择第一行第一列）
        :return:
        '''
        time.sleep(1)
        self.driver.find_ajax_id('main_menu')
        # self.driver.find_id('main_menu').click()
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('进行中订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/listOrderProcess.html' in self.driver.current_url,u'不是进行中订单页面')
        finally:
            pass
        self.driver.find_id('orderFlow').click()
        time.sleep(1)
        text=self.driver.find_id('gview_list2').find_class('ui-jqgrid-titlebar').text
        print text
        self.assertTrue(u'订单流程' in text,u'订单流程提示框不正确或不存在' )

        self.driver.find_class('xubox_close').click()
        time.sleep(1)
        isClose=True
        try:
            self.driver.find_id('gview_list2')
            isClose=False
        except self.driver.NoSuchElementException:
            isClose=True

        self.assertTrue(isClose,u'订单流程弹出框没有被关闭')



