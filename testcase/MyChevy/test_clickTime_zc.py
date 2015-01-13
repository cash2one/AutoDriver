# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep
import datetime
import time

from framework.core import device_bak, the


#再次点击时间控件，之前所选时间显示在时间控件中
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android

    def tearDown(self):
        #返回首页
        device_bak.switchToHome(self,self.mainActivity)

    def test_case1(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/iv_user_icon').click()
        sleep()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(5)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        button=self.driver.find_elements_by_class_name('android.widget.ImageButton')
        button[0].click()
        button[2].click()
        button[6].click()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        sleep(2)
        t1=self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').text
        #选择时间确定后，获取文本框中的时间
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        els=self.driver.find_elements_by_class_name('android.widget.EditText')
        year=int(els[0].text)
        #取第一个EditText为年，EditText为unicode,要转成int型
        mon=int(els[1].text[:-1])
        #取第二个EditText为月，[：-1]为取最后一个字符之前字符，即删去月
        day=int(els[2].text)
        #取第二个EditText为天
        hour=int(els[3].text)
        minute=int(els[4].text)
        t2=datetime.datetime(year,mon,day,hour,minute).timetuple()
         #前字符转换成datetime,再用.timetuple()转换成struct_time形式，
        d2=time.strftime("%Y-%m-%d %H:%M",t2)
        #格式化
        d1=str(t1)
        self.assertEqual(d1,d2)