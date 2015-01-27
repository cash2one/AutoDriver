# coding=utf-8
__author__ = 'xiaohengli@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_monitoringRefresh(self):
        '''
        列表刷新，系统重新加载数据，显示当前在线客户人数
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在客户监控上
        self.driver.find_element_by_link_text(u'客户监控').click()
        self.driver.find_id('query').click()




    def test_Drivermonitoring(self):
        '''
        点击下拉框,显示“全部”、“空闲”、“休息”、“服务中”
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        self.assertTrue(opts[0].text==u'全部')
        tuple=(u'全部',u'空闲',u'休息',u'服务中')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')
            print(type)
            if not type in tuple:
                isExist = False
                break
        self.assertTrue(isExist,'false')



    def test_DrivermonitoringAll(self):
        '''
        属性值“空闲”显示在文本框中
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        time.sleep(3)
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        for opt in opts:
            #判断text里面的内容等不等于空闲

            if opt.get_attribute('text')==u'空闲':
                opt.click()
                self.assertTrue(opt.is_selected())
            elif opt.get_attribute('text')==u'全部':
                opt.click()
                self.assertTrue(opt.is_selected())

            elif opt.get_attribute('text')==u'休息':
                opt.click()
                self.assertTrue(opt.is_selected())

            elif opt.get_attribute('text')==u'服务中':
                opt.click()
                self.assertTrue(opt.is_selected())
            elif opt.get_attribute('text')==u'全部':
                opt.click()
                self.assertTrue(opt.is_selected())

    def test_Drivermonitoringselect(self):
        '''
            在司机工号文本框中输入正常数量字符
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        #输入内容正常显示在文本框中
        self.driver.find_element_by_id('driverInfo').send_keys(u'小米')
        test=self.driver.find_element_by_id('driverInfo').get_attribute('value')
        self.assertEqual(test,u'小米',u'输入内容没有正常显示在文本框中')

    def test_Drivermonitoringtest(self):
        '''
        输入内容正常显示在文本框中
        限制长度以内的字符正常显示，超出限制长度的部分系统限制输入

        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        self.driver.find_element_by_id('driverInfo').send_keys(u'小米输入内容没有正常显示在文本框中输入内容没有正常显示在文本框中输入内容没有正常显示在文本框中')
        test=self.driver.find_element_by_id('driverInfo').get_attribute('value')
        self.assertEqual(test,u'小米输入内容没有正常显示在文本框中输入内容没有正常显示在文本框中输入内容没有正常显示在文本框中',u'输入内容没有正常显示在文本框中')


    def test_Drivermonitoringquery(self):
        '''
       列表中显示符合查询条件的所有在线司机的的监控记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        self.driver.find_id('query').click()

        self.driver.find_element_by_id('driverInfo').send_keys(u'140221')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[1].text
                self.assertEqual(text,u"140221",u'没有找到该司机工号')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)




    def test_DriveFuzzyquery(self):
        '''
        模糊查询  列表中显示符合查询条件的所有在线司机的的监控记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'系统监控')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'司机监控').click()
        self.driver.find_element_by_id('driverInfo').send_keys(u'14')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')
        if len(trs)>1:
            for i in range(1,len(trs)):
                text=trs[i].find_tags('td')[1].text
                self.assertTrue(text,u"14")
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)



