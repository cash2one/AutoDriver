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

    def test_weixin_info(self):
        '''
        添加微信响应信息，查看类型下拉框
        切换类型下拉框，下方显示相应的模块
        :return:
        '''
        above=self.driver.find_element_by_link_text(u'微信服务')

        self.driver.action_chains().move_to_element(above).perform()
        #鼠标悬停在统计查询
        self.driver.find_element_by_link_text(u'响应信息').click()
        print(self.driver.title)

        self.driver.find_id('add').click()
        opts=self.driver.find_id('weixinInfo_responseType').find_tags('option')
        self.assertTrue(opts[0].text==u'文本')
        tuple=(u'文本',u'图片',u'图文')
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
        weixin_img=self.driver.find_id('weixin_img')
        self.assertTrue(weixin_img.is_enabled(),u'未显示图片按钮')
        #响应类型选择图片，下方显示选择图片按钮
        time.sleep(3)

        for opt in opts:
            if opt.get_attribute('text')==u'文本':
                opt.click()
                self.assertTrue(opt.is_selected())
        content=self.driver.find_id('weixinInfo_content')
        self.assertTrue(content.is_enabled(),u'下放不显示文本框')
        #响应类型选择文本，下方显示文本内容文本框




