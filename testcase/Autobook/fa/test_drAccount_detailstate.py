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

    #司机账户明细收支状态查询（以司机工号140221为例）
    def test_drAccount_detailState(self):
        time.sleep(2)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('司机账户').click()
        time.sleep(2)

        self.driver.find_element_by_id('driverInfo').clear()
        self.driver.find_element_by_id('driverInfo').send_keys('140221')
        self.driver.find_element_by_id('query').click()#点击查询

        #table1为当前司机账户列表
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        trs1[1].find_element_by_id('view_driverAccount').click()#进入140221的收支明细列表界面中
        time.sleep(2)


        #点击收入
        self.driver.find_element_by_id('balanceState').find_elements_by_tag_name('option')[1].click()#点击收支框收入项
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出支出列，支出为0.00为真
        #定位当前列表
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        for i in range(1,len(trs2)):
            tds_pledgeOut = trs2[i].find_elements_by_tag_name('td')[5]
            tds_prepay = trs2[i].find_elements_by_tag_name('td')[8]
            tds_orderOut = trs2[i].find_elements_by_tag_name('td')[10]

            pledgeOut_text = tds_pledgeOut.get_attribute('title')#取出押金支出
            prepay_text = tds_prepay.get_attribute('title')#取出预付款支出
            orderOut_text = tds_orderOut.get_attribute('title')#取出订单支出

            #print pledgeOut_text,prepay_text,orderOut_text
            #self.assertTrue(self.driver.to_int(balanceOut_text) == 0,'msg')#将字符串转换成int型对比
            self.assertTrue(pledgeOut_text == '0.00',u'押金支出不为0')
            self.assertTrue(prepay_text == '0.00',u'预付款支出不为0')
            self.assertTrue(orderOut_text == '0.00',u'订单支出不为0')

        time.sleep(2)

        #取出收入的记录数
        pager_In = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table_last_In = self.driver.find_element_by_id('list')
        trs_last_In = table_last_In.find_elements_by_tag_name('tr')
        #正常状态下的司机记录数为
        In_No = (int(pager_In)-1)*20+len(trs_last_In)-1
        print '收入的记录数为:',In_No,'条'
        time.sleep(2)


        #点击支出
        self.driver.find_element_by_id('balanceState').find_elements_by_tag_name('option')[2].click()#点击收支框支出项
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出收入列，收入为0.00为真
        #定位当前列表
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)):
            tds_pledgeIn = trs3[i].find_elements_by_tag_name('td')[4]
            tds_prepayIn = trs3[i].find_elements_by_tag_name('td')[7]

            pledgeIn_text = tds_pledgeIn.get_attribute('title')#押金收入
            prepayIn_text = tds_prepayIn.get_attribute('title')#取出预付款收入

            #print pledgeIn_text,prepayIn_text
            self.assertTrue(self.driver.to_int(pledgeIn_text) == 0,u'押金收入不为0')#将字符串转换成int型对比
            self.assertTrue(self.driver.to_int(prepayIn_text) == 0,u'预付款收入不为0')#将字符串转换成int型对比

        time.sleep(2)

        #取出支出的记录数
        pager_Out = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table_last_Out = self.driver.find_element_by_id('list')
        trs_last_Out = table_last_Out.find_elements_by_tag_name('tr')
        #正常状态下的司机记录数为
        Out_No = (int(pager_Out)-1)*20+len(trs_last_Out)-1
        print '支出的记录数为：',Out_No,'条'
        time.sleep(2)

        #点击收支
        self.driver.find_element_by_id('balanceState').find_elements_by_tag_name('option')[0].click()#点击收支
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出全部收支的记录数
        pager_all = self.driver.find_element_by_id('sp_1_pager').text
        #点击最后一页，取出最后一页的列表长度
        self.driver.find_element_by_id('last_pager').click()
        time.sleep(1)
        table_last_all = self.driver.find_element_by_id('list')
        trs_last_all = table_last_all.find_elements_by_tag_name('tr')
        #全部收支状态下记录数为
        all_No = (int(pager_all)-1)*20+len(trs_last_all)-1
        print '全部收支状态下的记录数为：',all_No,'条'
        time.sleep(2)
        #对比：全部收支状态下记录数 =收入记录数 + 支出记录数，为真
        self.assertTrue(all_No == In_No + Out_No,u'总记录数不等于收入数加支出数' )
