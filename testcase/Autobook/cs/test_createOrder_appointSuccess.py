# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *
DRIVER=u'小米'

class TestCase(unit.TestCase):
    '''
    指定司机下单成功（订单数为默认1）
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_appoint_orderSuccess(self):
        '''
        #点击创建订单跳转到创建订单界面
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
        #self.driver.find_id('divid1').find_tags('tr')[0].find_tags('td')[0].click()
        time.sleep(3)

        # 选择周边下单
        opts=self.driver.find_id('orderType').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'指定下单':
                opt.click()
        time.sleep(2)
        #点击选择司机
        self.driver.find_id('select_driver_btn').click()
        self.driver.find_ajax_id('near_driver_list')
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
                break
            else:
                print(u'没找到司机小米')
        time.sleep(3)
        self.driver.find_id('sure_btn').click()

        #创建订单按钮
        self.driver.find_id('create_order_btn').click()
        time.sleep(3)
        #弹出订单窗口
        self.driver.switch_to_alert()
        text=self.driver.find_class('xubox_dialog').text
        print text
        #点击弹出订单窗口中确定按钮，跳转到进行中订单
        self.driver.find_link('确定').click()
        time.sleep(5)
        #获取进行中订单的订单号
        trs=self.driver.find_id('list').find_tags('tr')
        for i in range(1,len(trs)-1):
            tds=trs[i].find_tags('td')[1]
            print tds.text
            self.assertTrue(tds.text in text,u'两个订单号不匹配')



