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

    def test_logParameter(self):
        '''
        在请求参数文本框中输入部分参数值,接口日志列表中显示包含该参数值的所有日志记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #在请求参数文本框里面输入aaaaa
        self.driver.find_element_by_id('params').send_keys(u'aaaaa')
        self.driver.find_element_by_id('query').click()
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')
        print len(trs)
        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text=trs[i].find_tags('td')[6].text
                #判断是不是td里面的  请求参数是不是aaaaa
                self.assertTrue(u'aaaaa'in text)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

    def test_logReques(self):
        '''
                      在请求号文本框中输入全部字符, 接口日志列表中显示请求号为输入内容的日志记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #在请求号文本框里面输入14017814213006828048340
        self.driver.find_element_by_id('requestIdSearch').send_keys('14017814213006828048340')
        self.driver.find_element_by_id('query').click()
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')

        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text=trs[i].find_tags('td')[8].text
                #判断是不是td里面的  请求号是不是14017814213006828048340
                print text,i
                self.assertTrue('14017814213006828048340' in text)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_logException(self):
        '''
       在异常内容文本框中输入全部字符,接口日志列表中显示异常内容为输入内容的日志记录
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'日志查询')
        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在日志查询上
        self.driver.find_element_by_link_text(u'接口访问日志').click()
        #在异常内容文本框里面输入u'{"res":"-2031","msg":"令牌失效"}'
        self.driver.find_element_by_id('content').send_keys(u'{"res":"-2031","msg":"令牌失效"}')
        self.driver.find_element_by_id('query').click()
        time.sleep(3)
        trs=self.driver.find_element_by_id('list').find_tags('tr')

        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in range(1,len(trs)):
                #找到td
                text=trs[i].find_tags('td')[9].text
                #判断是不是td里面的  请求参数是不是res":"-2031","msg":"令牌失效
                print text,i
                self.assertTrue(u'{"res":"-2031","msg":"令牌失效"}' in text)
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)





