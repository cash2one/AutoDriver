# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *


text=u'TEXT_BASIC_IIIEGAL'
#响应信息
class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_weixin_add(self):
        '''
        添加微信响应信息，添加成功查看是否显示在列表中，默认响应信息是否正确
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')
        self.driver.action_chains().move_to_element(above).perform()

        #鼠标悬停在微信服务
        self.driver.find_element_by_link_text(u'响应信息').click()
        self.assertEqual(self.driver.title,u'微信响应信息列表',u'没有进入对应页面')

        self.driver.find_id('add').click()
        print self.driver.title
        opts=self.driver.find_id('weixinInfo_responseCode').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==text:
                opt.click()
                self.assertTrue(opt.is_selected())

        desc=self.driver.find_id('info_desc').text

        opts1=self.driver.find_id('weixinInfo_responseType').find_tags('option')
        for opt1 in opts1:
            if opt1.get_attribute('text')==u'图片':
                opt1.click()
                self.assertTrue(opt1.is_selected())
        self.driver.find_id('file').send_keys('F:\weixin.jpg')

        self.driver.find_id('weixinInfoSubmit').click()
        self.assertEqual(u'微信响应信息列表页面',self.driver.title,u'没有进入对应页面')
        trs=self.driver.find_id('list').find_tags('tr')

        for i in range(1,len(trs)):
            txt1=trs[i].find_tags('td')[2].text
            txt2=trs[i].find_tags('td')[3].text
            if txt1==text:
                self.assertEqual(txt2,desc,u'默认响应信息显示不正确')
                break


    def test_weixin_edit(self):
        '''
        修改信息标题为text=u'TEXT_BASIC_IIIEGAL'的响应信息，修改成功
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')
        self.driver.action_chains().move_to_element(above).perform()

        #鼠标悬停在微信服务
        self.driver.find_element_by_link_text(u'响应信息').click()
        trs=self.driver.find_id('list').find_tags('tr')
        for i in range(1,len(trs)):
            txt1=trs[i].find_tags('td')[2].text
            tds=trs[i].find_tags('td')
            if txt1==text:
                tds[len(tds)-1].find_link(u'编辑').click()
                break
        self.assertEqual(u'编辑微信响应信息',self.driver.title,u'没有进入对应页面')
        opts=self.driver.find_element_by_id('weixinInfo_responseType').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'文本':
                opt.click()
                self.assertTrue(opt.is_selected())
        self.driver.find_element_by_id('weixinInfo_content').send_keys(u'编辑微信响应信息')
        self.driver.find_element_by_id('weixinInfoSubmit').click()
        self.assertEqual(u'微信响应信息列表页面',self.driver.title,u'没有进入对应页面')

        trs=self.driver.find_element_by_id('list').find_tags('tr')

        for i in range(1,len(trs)):
            txt1=trs[i].find_tags('td')[2].text
            txt2=trs[i].find_tags('td')[4].text
            txt3=trs[i].find_tags('td')[5].text
            if txt1==text:
                self.assertEqual(txt2,u'文本',u'信息类型显示不正确')
                self.assertEqual(txt3,u'编辑微信响应信息',u'响应信息显示不正确')
                break


    def test_weixin_delete(self):
        '''
        修改信息标题为text=u'TdeleteEXT_BASIC_IIIEGAL'的响应信息，修改成功
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')
        self.driver.action_chains().move_to_element(above).perform()

        #鼠标悬停在微信服务
        self.driver.find_element_by_link_text(u'响应信息').click()
        trs=self.driver.find_id('list').find_tags('tr')
        for i in range(1,len(trs)):
            txt1=trs[i].find_tags('td')[2].text
            tds=trs[i].find_tags('td')
            if txt1==text:
                tds[len(tds)-1].find_link(u'删除').click()
                break
        self.driver.switch_to_alter()
        self.driver.find_element_by_link_text(u'确定').click()











