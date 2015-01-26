# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_weixin_type(self):
        '''
        响应信息列表页面，查看类型下拉框
        选择类型为“图片”，列表中显示类型为图片的数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'响应信息').click()
        opts=self.driver.find_id('weixinType').find_tags('option')
        self.assertTrue(opts[0].text==u'全部类型')
        tuple=(u'全部类型',u'文本',u'图片',u'图文')
        isExit=True
        for opt in opts:
            text=opt.get_attribute('text')
            if not text  in tuple:
                isExit=False
        self.assertTrue(isExit,u'不存在元组中的字段')

        for opt in opts:
            if opt.get_attribute('text')==u'图片':
                opt.click()
                self.assertTrue(opt.is_selected())


        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):

                type=trs[i].find_tags('td')[4].text
                self.assertEqual(type,u'图片',u'列表中查询出的数据类型不是图片')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)


    def test_weixin_content(self):
        '''
        查询内容为‘验证码’，列表中显示查询出的数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'响应信息').click()
        self.driver.find_id('weixinInfo').send_keys(u'验证码')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):

                text=trs[i].find_tags('td')[5].text
                self.assertTrue(u'验证码' in text,u'列表中查询出的内容不包含验证码')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)



    def test_weixin(self):
        '''
        查询类型为‘文本’内容为‘验证码’，列表中显示查询出的数据
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')
        self.driver.action_chains().move_to_element(above).perform()
        self.driver.find_element_by_link_text(u'响应信息').click()
        opts=self.driver.find_id('weixinType').find_tags('option')
        for opt in opts:
            if opt.get_attribute('text')==u'文本':
                opt.click()
                self.assertTrue(opt.is_selected())
        self.driver.find_id('weixinInfo').send_keys(u'验证码')
        self.driver.find_id('query').click()
        trs=self.driver.find_id('list').find_tags('tr')

        if len(trs)>1:
            for i in range(1,len(trs)):

                text=trs[i].find_tags('td')[5].text
                type=trs[i].find_tags('td')[4].text
                self.assertEqual(type,u'文本',u'列表中查询出的数据类型不是文本')
                self.assertTrue(u'验证码' in text,u'列表中查询出的内容不包含验证码')
        else:
            text=self.driver.find_class('norecords').text
            self.assertTrue(u'没有符合条件的数据'in text)

