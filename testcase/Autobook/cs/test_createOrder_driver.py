# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'


import time
from drivers import *
DRIVER=u'小米'

class TestCase(unit.TestCase):
    '''
    指定司机下单(重复选择同一个司机、至少选择一位司机)
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_repeatedSelection_driver(self):
        '''
        #选择重复的司机
        :return:
        '''
        time.sleep(2)
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
        ul=self.driver.find_id('near_driver_list').find_tag('ul')
        li=ul.find_tags('li')
        for d in range(0,len(li)):
            els=li[d]
            name=els.find_class('driver_name').text
            if DRIVER in name:
                els.click()
                els.click()
                break
            else:
                print(u'没找到司机小米')
        time.sleep(3)
        text=self.driver.find_class('xubox_dialog').text
        self.assertEqual(text,u'小米 已选，请选择其他司机','提示信息不正确')



    def test_driverNull(self):
        '''
        #不选择司机，直接点击确定按钮
        :return:
        '''
        self.driver.find_ajax_id('main_menu')
        self.driver.find_id('main_menu').click()
        # print menu
        #
        # for i in range(0,len(menu)-1):
        #     if menu[i]==u'订单管理':
        self.driver.find_link('订单管理').click()
        time.sleep(3)
        self.driver.find_link('创建订单').click()
        time.sleep(5)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'该页面不是创建订单页面')
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
        #在选择司机页面直接点击确定按钮
        self.driver.find_id('sure_btn').click()
        text=self.driver.find_class('xubox_dialog').text
        self.assertEqual(text,u'请至少选择一位司机',u'提示框中内容不相等')

