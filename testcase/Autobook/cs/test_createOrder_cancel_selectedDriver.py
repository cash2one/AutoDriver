# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    指定司机下单(取消已选择的司机、在选择司机页面点击返回)
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_cancel_driver(self):
        '''
        选择所有的司机并取消所选择的司机，点击确定按钮提示“至少选择一位司机”
        :return:
        '''
        self.driver.find_ajax_id('main_menu')
       #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('创建订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)

        #填写信息
        self.driver.find_id('customerCall').send_keys('wss')
        self.driver.find_id('phone').send_keys('13500000000')
        self.driver.find_id('map_search_btn').click()
        #输入客户位置
        self.driver.find_id('keyword').send_keys(u'万源路')
        self.driver.find_id('search_btn').click()
        #选择客户位置
        #self.driver.find_ajax_id('result')
        self.driver.find_element_by_xpath('//*[@id="divid1"]/table/tbody/tr/td[1]/img').click()
        time.sleep(3)
        #点击选择司机按钮
        self.driver.find_id('select_driver_btn').click()
        self.driver.find_ajax_id('near_driver_list')
        #判断列表中是否有司机
        nearbyrivers = []
        try:
              nearbyrivers=self.driver.find_classes('driver_detail_on_list')
        except self.driver.NoSuchElementException:
            pass
        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')
        #选择列表中所有的司机
        ul=self.driver.find_id('near_driver_list').find_tag('ul')
        li=ul.find_tags('li')
        for d in range(0,len(li)):
            els=li[d]
            els.find_class('driver_name').click()
        time.sleep(3)
        #取消被选中的司机
        dr=self.driver.find_id('selected_driver_list').find_classes('selectd_name')
        for i in range(0,len(dr)):
            dr[i].find_class('cancel_btn').click()
        #点击确定按钮，判断没有选中的司机
        self.driver.find_id('sure_btn').click()
        text=self.driver.find_class('xubox_dialog').text
        self.assertTrue(text==u'请至少选择一位司机',u'没有选择司机，没有提示信息或提示信息不正确')



    def test_return_createOrder(self):
        '''
        在选择司机页面点击返回按钮，返回到创建订单页面
        :return:
        '''
        self.driver.find_ajax_id('main_menu')
        self.driver.find_id('main_menu').click()
        #选择订单管理
        self.driver.find_link('订单管理').click()
        time.sleep(3)
        self.driver.find_link('创建订单').click()
        time.sleep(5)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)

        #填写信息
        self.driver.find_id('customerCall').send_keys('wss')
        self.driver.find_id('phone').send_keys('13500000000')
        self.driver.find_id('map_search_btn').click()
        #输入客户位置
        self.driver.find_id('keyword').send_keys(u'万源路')
        self.driver.find_id('search_btn').click()
        #选择客户位置
        #self.driver.find_ajax_id('result')
        self.driver.find_element_by_xpath('//*[@id="divid1"]/table/tbody/tr/td[1]/img').click()
        time.sleep(3)
        #点击选择司机按钮
        self.driver.find_id('select_driver_btn').click()
        #在选择司机页面点击返回按钮
        self.driver.find_id('back_btn').click()
        #判断是否返回到了创建订单页面
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            print '跳转的页面不正确'


