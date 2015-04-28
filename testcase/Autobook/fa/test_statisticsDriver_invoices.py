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

    #司机出入账,查询：是否已打印发票
    def test_statisticsDriver_invoices(self):
        '''
        司机出入账,查询：是否已打印发票(含已打印、未打印)
        :return:
        '''
        time.sleep(2)
        self.driver.find_element_by_link_text('统计报表').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('司机出入账').click()
        time.sleep(2)

        #self.driver.find_element_by_id('year').click()
        self.driver.find_element_by_id('year').find_elements_by_tag_name('option')[3].click()#选择2013年


        time.sleep(4)

        #self.driver.find_element_by_id('year').click()
        self.driver.find_element_by_id('year').find_elements_by_tag_name('option')[4].click()#选择2014年
        self.driver.find_element_by_id('statistics').click()#点击统计，进入司机出入账列表界面
        time.sleep(3)


        self.driver.find_element_by_id('invoices').find_elements_by_tag_name('option')[2].click()#选择未打印
        self.driver.find_element_by_id('query').click()#点击查询query
        time.sleep(1)
        table_NoPrint = self.driver.find_element_by_id('list')
        trs1 = table_NoPrint.find_elements_by_tag_name('tr')
        trs1[1].find_element_by_class_name('print').click()#点击打印
        time.sleep(1)
        self.driver.find_class('xubox_main').find_class('xubox_yes').click()#点击确定
        time.sleep(1)
        self.driver.find_element_by_id('query').click()#点击查询query

        #未打印的司机出入账列表，打印次数为0
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)):
            tds_PrintNo = trs3[i].find_elements_by_tag_name('td')[7]
            PrintNo_text = tds_PrintNo.get_attribute('title')#取出打印次数

            self.assertTrue(self.driver.to_int(PrintNo_text) == 0,u'打印次数不为0')#将字符串转换成int型对比

        time.sleep(2)

        #取出未打印的司机出入账列表的记录数
        pager_NoPrint = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table_last_NoPrint = self.driver.find_element_by_id('list')
        trs_last_NoPrint = table_last_NoPrint.find_elements_by_tag_name('tr')
        #未打印的司机出入账列表的记录数为
        NoPrint_No = (int(pager_NoPrint)-1)*20+len(trs_last_NoPrint)-1
        print '未打印记录数为：',NoPrint_No,'条'
        time.sleep(2)


        self.driver.find_element_by_id('invoices').find_elements_by_tag_name('option')[1].click()#选择未打印
        self.driver.find_element_by_id('query').click()#点击查询query
        time.sleep(2)
        #取出已打印的司机出入账列表的记录数
        pager_Print = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table_last_Print = self.driver.find_element_by_id('list')
        trs_last_Print = table_last_Print.find_elements_by_tag_name('tr')
        #未打印的司机出入账列表的记录数为
        Print_No = (int(pager_Print)-1)*20+len(trs_last_Print)-1
        print '已打印记录数为：',Print_No,'条'
        time.sleep(2)


        self.driver.find_element_by_id('invoices').find_elements_by_tag_name('option')[0].click()#选择是否打印发票
        self.driver.find_element_by_id('query').click()#点击查询query
        time.sleep(2)
        #取出司机出入账的全部记录数
        pager_all = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table_last_all = self.driver.find_element_by_id('list')
        trs_last_all = table_last_all.find_elements_by_tag_name('tr')
        #司机出入账的全部记录数为
        all_No = (int(pager_all)-1)*20+len(trs_last_all)-1
        print '全部司机出入账的记录数为：',all_No,'条'
        time.sleep(2)
        #对比：全部收支状态下记录数 =收入记录数 + 支出记录数，为真
        self.assertTrue(all_No == NoPrint_No + Print_No,u'全部收支状态下记录数不等于收入记录数加支出记录数' )

