# coding=utf-8
__author__ = 'zhangchun'
import unittest
from time import sleep
import datetime

from framework.core import device_bak, the


#查看时间控件
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
        sleep(3)
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_name').send_keys('gsd')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_phone').send_keys('13800000002')
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/user_ok').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_ok').click()
        #登录成功
        sleep(7)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/btn_order').click()
        sleep(3)
        self.driver.find_element_by_id('cn.com.pathbook.mychevy:id/tv_order_time').click()
        self.driver.switch_to_alert()
        els=self.driver.find_elements_by_class_name('android.widget.EditText')
        year=int(els[0].text)
        #取第一个EditText为年，EditText为unicode,要转成int型
        mon=int(els[1].text[:-1])
        #取第二个EditText为月，[：-1]为取最后一个字符之前字符，即删去月
        day=int(els[2].text)
        #取第二个EditText为天
        #t1=datetime.datetime(year,mon,day).timetuple()
        #将字符转换成日期形式，转成struct_time
        # d1=time.strftime("%Y/%m/%d",t1)  再格式化
        # t2=datetime.date.today() + datetime.timedelta(days=1)
        # d2=time.strftime("%Y/%m/%d",t2.timetuple())
        # self.assertEqual(d1,d2)
        t1=datetime.date(year,mon,day)#将字符转换成日期形式
        t2=datetime.date.today() + datetime.timedelta(days=1)
        #t2为系统日期的后一天日期
        self.assertEqual(t1,t2)
