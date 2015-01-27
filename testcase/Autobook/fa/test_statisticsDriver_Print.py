# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

    #司机出入账,打印，打印次数自动加  1
    def test_statisticsDriver_Print(self):
        '''
        司机出入账,打印，打印次数自动加1
        :return:
        '''
        time.sleep(2)
        self.driver.find_element_by_link_text('统计报表').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('司机出入账').click()
        time.sleep(2)

        #self.driver.find_element_by_id('year').click()
        self.driver.find_element_by_id('year').find_elements_by_tag_name('option')[3].click()#选择2013年
        time.sleep(1)
        #self.driver.find_element_by_id('year').click()
        self.driver.find_element_by_id('year').find_elements_by_tag_name('option')[4].click()#选择2014年
        time.sleep(1)
        self.driver.find_element_by_id('statistics').click()#点击统计，进入司机出入账列表界面
        time.sleep(1)


        self.driver.find_element_by_id('invoices').find_elements_by_tag_name('option')[0].click()#选择是否打印发票
        self.driver.find_element_by_id('query').click()#点击查询query
        time.sleep(2)

        #取出打印之前的打印次数
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        printNum = trs[1].find_elements_by_tag_name('td')[7]
        printNum_text = printNum.get_attribute('title')
        print printNum_text
        trs[1].find_class('print').click()#点击第一行的打印
        time.sleep(2)
        table_msg = self.driver.find_class('xubox_main')
        msg_text = table_msg.find_class('xubox_text').text
        print msg_text
        self.assertTrue(u'确定打印发票' in msg_text,u'没有找到指定字符')
        table_msg.find_class('xubox_yes').click()#点击确定
        time.sleep(3)

        #取出打印之后的打印次数
        self.driver.find_element_by_id('query').click()#点击查询query刷新页面
        time.sleep(2)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        printNum2 = trs2[1].find_elements_by_tag_name('td')[7]
        printNum_text_new = printNum2.get_attribute('title')
        print printNum_text_new
        #比较打印前后的次数打印后自动加1，先将次数转换成int型。
        self.assertTrue(int(printNum_text_new) == int(printNum_text) + 1,u'打印次数没有自动加1')
        # if int(printNum_text_new) == int(printNum_text) + 1:
        #     print 'Ture'
        # else:
        #     print 'False'

        time.sleep(2)

