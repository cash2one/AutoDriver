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

    def test_logPulldown(self):
        '''
        下拉框中显示所有平台的id值
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        opts=self.driver.find_element_by_id('platformId').find_tags('option')
        self.assertTrue(opts[0].text==u'平台Id')
        tuple=(u'平台Id','APP_001','CS_001','CYL_OP_001','HEART_001','HR_001','HZL_HEART_001','HZL_HR_001','HZL_OP_001','IS_001','LCH_CS_001',
               'LXJ_CS_001','LXJ_HEART_001','LXJ_IS_001','LXJ_OP_001','NBY_APP_001','NBY_OP_001','OP_001','OP_002','STC_APP_001','STC_HEART_001',
               'STC_HR_001','STC_OP_001','ZCJ_CS_001','ZCJ_OP_001','ZMM_APP_001','ZMM_HEART_001','ZMM_HR_001','ZMM_OP_001')
        isExist =True
        for opt in opts:
            type=opt.get_attribute('text')
            print(type)
            if not type in tuple:
                isExist = False
                break
        self.assertTrue(isExist,'false')
        #查看日志类型下拉框中的选项


    def test_logPullselect(self):
        '''
        点击某个选项，该选项回显在文本框中
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        opts=self.driver.find_element_by_id('platformId').find_tags('option')

        for opt in opts:
            #判断text里面的内容等不等于客服专员
            if opt.get_attribute('text')=='APP_001':  #获取对象属性
                opt.click()


            else:
                opt.get_attribute('text')==u'平台Id'
                opt.click()

    def test_logResult(self):
        '''
        下拉框中显示“结果”、“成功”、“失败”
        限制长度以内的字符正常显示，超出限制长度的部分系统限制输入
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #下拉框里面成功或者失败
        opts=self.driver.find_element_by_id('result').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'成功':
               opt.click()

            else:
               opt.get_attribute('text')==u'失败'
               opt.click()
        time.sleep(1)
        #接口名称
        self.driver.find_element_by_id('serviceName').send_keys(u'driverService.refreshLocationdriverService.refreshLocationdriverService.refreshLocation')
        time.sleep(1)
        #请求参数
        self.driver.find_element_by_id('params').send_keys(u'driverService.refreshLocationdriverService.refreshLocationdriverService.refreshLocation')
        time.sleep(1)
        #请求号超长
        self.driver.find_element_by_id('requestIdSearch').send_keys(u'driverService.refreshLocationdriverService.refreshLocationdriverService.refreshLocation')

    def test_logselect(self):
        '''
            空值查询
        :return:
        '''
        #空条件查询
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        time.sleep(1)
        #点击查询
        self.driver.find_element_by_id('query').click()

    def test_logselectName(self):
        '''
        接口日志列表中显示该名称的的所有日志记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()

        self.driver.find_element_by_id('serviceName').send_keys(u'driverService.dealOrder')
        self.driver.find_element_by_id('query').click()
         #找到对应的td
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')
        print len(trs)
        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text=trs[i].find_tags('td')[5].text
                #判断是不是td里面的接口名称是不是driverService.dealOrder
                print text,i
                self.assertEqual(text,u"driverService.dealOrder",u'接口中没有这个值')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

    def test_logseleID(self):
        '''
        根据id查询显示该id的的所有日志记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
         #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        opts=self.driver.find_element_by_id('platformId').find_tags('option')
        for opt in opts:
         #判断下拉列表里面的是不是禁用
            if opt.get_attribute('text')==u'APP_001':  #获取对象属性
                opt.click()
                self.assertTrue(opt.is_selected())
        self.driver.find_element_by_id('query').click()
         #找到对应的td
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')
        print len(trs)
        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text=trs[i].find_tags('td')[4].text
                print text,i
                self.assertEqual(text,u"APP_001" ,u'没有找到改id')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)
