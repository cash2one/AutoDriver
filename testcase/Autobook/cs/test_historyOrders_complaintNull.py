# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
from drivers import *
ORDER=u'15012610598594'
COMPLAINT=u'投诉内容不能为空.'
RESULT=u'调查结果不能为空.'

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_complaintNull(self):
        '''
        投诉的内容空
        :return:
        '''
        time.sleep(2)
        self.driver.find_ajax_id('main_menu')
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('历史订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/listOrderHistory.html' in self.driver.current_url,u'不是历史订单页面')
        finally:
            pass
        self.driver.find_id('orderNo').send_keys(ORDER)
        #点击查询按钮
        self.driver.find_id('query').click()
        time.sleep(1)
        trs=self.driver.find_id('list').find_tags('tr')
        tds=trs[1].find_tags('td')
        if ORDER in tds[1].text:
            try:
                tds[9].find_id('complaint').click()
                time.sleep(1)
            except self.driver.NoSuchElementException:
                pass

        try:
            #判断跳转的页面是否是客户投诉页面
            self.assertTrue('http://192.168.3.31/cs/cs/orderInform/addOrderInform.html' in self.driver.current_url,u'不是客户投诉页面')
        finally:
            pass
        #点击提交按钮
        self.driver.find_id('complainSubmit').click()
        #判断投诉内容为空时，提示信息是否正确
        contents_complaint=self.driver.find_id('informVo_content_tip').text
        self.assertEqual(contents_complaint,COMPLAINT,u'投诉内容为空时提示信息不正确或不存在')

        #判断调查结果为空时，提示信息是否正确
        results_survey=self.driver.find_id('content_tip').text
        self.assertEqual(results_survey,RESULT,u'调查结果为空时提示信息不正确或不存在')
