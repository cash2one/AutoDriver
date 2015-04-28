# coding=utf-8
__author__ = 'zhangchun'

import time
from drivers import *

#查看距离活动开始时间是否正确
class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_name(u'聚乐会').click()
        time.sleep(10)
        txt1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_newpartydistancetime').text

        t1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_newpartytime').text
        t= time.strptime(t1,"%Y/%m/%d")
        #将获取的活动开始时间转换成string型，strptime以指定格式从文本描述中解析出时间
        d1=time.mktime(time.localtime())
        #time.localtime()获取当前时间。time.mktime(）将时间转换成秒
        d2=time.mktime(t)
        tm=(d2-d1)/(60*60*24)
        if tm>1:
            txt=int(tm)#若距离开始时间大于1天则显示天数，int()为取整
        else:
            tm=(d2-d1)/(60*60)#若小于1天则显示小时数
            txt=int(tm)

        self.assertTrue(str(txt) in txt1)

