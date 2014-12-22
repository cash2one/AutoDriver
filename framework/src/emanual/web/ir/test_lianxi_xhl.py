__author__ = 'xhl'
# coding=utf-8
#hr_循环添加司机多选框测试lll
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login('role_admin')

    def tearDown(self):
        #返回首页
        self.driver.close()

    #查询（角色）
    def test_my_info(self):
        #查询找到对应下拉列表的名字
        opts=self.driver.find_element_by_id('role').find_elements_by_tag_name('option')
        for opt in opts:
            #判断下拉列表里面的是不是客服专员
            if opt.get_attribute('text')==u'客服专员':  #获取对象属性
                opt.click()
        #选择了客服专员点击查询
        self.driver.find_element_by_id('query').click()
        time.sleep(10)
        #找到对应的table的tr里面的td
        tes=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[5].text
        print tes
        #判断名字是不是客服专员
        self.assertEqual(tes,u'客服专员')

    #查询（状态）
    def test_my_select(self):
         #查询找到对应下拉列表的名字
         opts=self.driver.find_element_by_id('status').find_elements_by_tag_name('option')
         for opt in opts:
         #判断下拉列表里面的是不是禁用
            if opt.get_attribute('text')==u'禁用':  #获取对象属性
                opt.click()
                 #选择了禁用点击查询
         self.driver.find_element_by_id('query').click()
         time.sleep(4)
         #找到对应table下面的tr
         trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #判断长度是不是小于1
         if len(trs)>1:
            #循环行
            for i in (1,len(trs)-1):
                #找到td
                text=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[i].find_elements_by_tag_name('td')[6].text
                #判断是不是td里面的状态是不是已禁用
                self.assertEqual(text,u"已禁用")
         else:
            pass


    def test_my_sele(self):
        opts=self.driver.find_element_by_id('role').find_elements_by_tag_name('option')
        for opt in opts:
            #判断下拉列表里面的是不是客服专员
            if opt.get_attribute('text')==u'客服专员':  #获取对象属性
                opt.click()
        #查询找到对应下拉列表的名字
        op=self.driver.find_element_by_id('status').find_elements_by_tag_name('option')
        time.sleep(4)
        tes=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[5].text
        print tes
        #判断名字是不是客服专员
        self.assertEqual(tes,u'客服专员')
        for ops in op:
         #判断下拉列表里面的是不是禁用
            if ops.get_attribute('text')==u'禁用':  #获取对象属性
                ops.click()

        self.driver.find_element_by_id('query').click()
        time.sleep(4)
        #找到对应table下面的tr
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #判断长度是不是小于1
        if len(trs)>1:
            #循环行
            for i in (1,len(trs)-1):
                #找到td
                text=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[i].find_elements_by_tag_name('td')[6].text
                #判断是不是td里面的状态是不是已禁用
                self.assertEqual(text,u"已禁用")
        else:
            pass

    def test_my_up(self):
        #找到对应的option
        opts=self.driver.find_element_by_id('role').find_elements_by_tag_name('option')
        for opt in opts:
            #判断text里面的内容等不等于客服专员
            if opt.get_attribute('text')==u'客服专员':  #获取对象属性
                opt.click()


        #点击重置
        op=self.driver.find_element_by_id('status').find_elements_by_tag_name('option')

        tes=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[5].text
        #判断名字是不是客服专员
        self.assertEqual(tes,u'客服专员')
        for ops in op:
         #判断下拉列表里面的是不是禁用
            if ops.get_attribute('text')==u'禁用':  #获取对象属性
                ops.click()
        time.sleep(3)
        self.driver.find_element_by_id('resetValue').click()

    def test_my_reset(self):
        #找到td里面的状态
        text=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[6].text
        #找到对应的td
        td=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[7]
        if text==u'正常':
            #找到td下面的a标签
            td.find_elements_by_link_text(u'禁用')[0].click()
        else:
            #找到td下面的a标签
            td.find_elements_by_link_text(u'启用')[0].click()
            #弹出框的确定
        dr=self.driver.switch_to_alert()
        dr.accept()
        time.sleep(4)



    #编辑
    def test_my_update(self):
        td=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[7]
        td.self.driver.find_element_by_id('status').find_elements_by_tag_name('option')
    #添加（查询)
    def test_my_into(self):
        self.driver.find_element_by_id('add').click()
        self.driver.find_element_by_id('operatorInfo').send_keys(u'你好')
        time.sleep(3)
        self.driver.find_element_by_id('querychildList').click()


    def test_my_into_select(self):

        self.driver.find_element_by_id('add').click()
        self.driver.find_ajax_id("operatorInfo")
        self.driver.find_element_by_id('operatorInfo').send_keys(u'你好啊')
        self.driver.find_element_by_id('resetValues').click()
        time.sleep(10)









