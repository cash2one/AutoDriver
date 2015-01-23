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

    #司机出入账,查询：司机工号查询，司机姓名查询
    def test_statisticsDriver_driverInfo(self):
        '''
        司机出入账,查询：司机工号查询，司机姓名查询
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


        #1.司机工号查询
        self.driver.find_element_by_id('driverNo').clear()
        self.driver.find_element_by_id('driverNo').send_keys(u'140017')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出工号列文本，对比信息是否正确
        #定位到当前列表
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        for i in range(1,len(trs1)):
            tds1 = trs1[i].find_elements_by_tag_name('td')[0]
            driverNo_text = tds1.get_attribute('title')
            self.assertTrue('140017' in driverNo_text,'msg')
            self.assertTrue(len(trs1) == 2,'msg')#工号是唯一的，只有一条记录
        time.sleep(2)

        #2.姓名查询
        self.driver.find_element_by_id('driverNo').clear()
        self.driver.find_element_by_id('driverName').clear()
        self.driver.find_element_by_id('driverName').send_keys(u'徐小七')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出姓名列文本，对比信息
        #定位到当前列表
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        for i in range(1,len(trs2)):
            tds2 = trs2[i].find_elements_by_tag_name('td')[1]
            driverName = tds2.get_attribute('title')
            self.assertTrue(u'徐小七' in driverName,'msg')
        time.sleep(2)

        #3.司机工号的模糊查询
        self.driver.find_element_by_id('driverName').clear()
        self.driver.find_element_by_id('driverNo').clear()
        self.driver.find_element_by_id('driverNo').send_keys('1400')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出手机号列文本，对比信息
        #定位到当前列表
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs3)):
            tds3 = trs3[i].find_elements_by_tag_name('td')[0]
            driverNo = tds3.get_attribute('title')
            self.assertTrue('1400' in driverNo,'msg')
        time.sleep(2)

        #4.司机姓名的模糊查询
        self.driver.find_element_by_id('driverNo').clear()
        self.driver.find_element_by_id('driverName').clear()
        self.driver.find_element_by_id('driverName').send_keys(u'张')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出姓名列文本，对比信息
        #定位到当前列表
        table4 = self.driver.find_element_by_id('list')
        trs4 = table4.find_elements_by_tag_name('tr')
        for i in range(1,len(trs4)):
            tds4 = trs4[i].find_elements_by_tag_name('td')[1]
            driverName1 = tds4.get_attribute('title')
            self.assertTrue(u'张' in driverName1,'msg')
        time.sleep(2)

        #5.无结果查询
        self.driver.find_element_by_id('driverNo').clear()
        self.driver.find_element_by_id('driverName').clear()
        self.driver.find_element_by_id('driverName').send_keys(u'自动化测试')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        #取出提示信息，对比信息
        norecords_text = self.driver.find_element_by_class_name('norecords').text
        self.assertTrue(u'没有符合条件的数据...' in norecords_text,'msg')
        time.sleep(2)
