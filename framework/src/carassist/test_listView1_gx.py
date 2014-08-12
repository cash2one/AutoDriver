# coding=utf-8
__author__ = 'gaoxu'
import unittest
from time import sleep
from framework.core import the,device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.android()

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)

    def activity(self):
     sleep(15)
        #每个测试用例，都需要把首页加入到变量mainActivity
     self.mainActivity = self.driver.current_activity

        #点击纯正附件
    def test_case1(self):
         #调用activity方法
        self.activity()
         #获取id并点击
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton3').click()

    def test_case2(self):
        self.test_case1()
        #第一级所有目录
        listView1=self.driver.find_element_by_id('cn.com.pathbook.carassist:id/listView1')
         #第一级目录第一个
        Layout=listView1.find_elements_by_class_name('android.widget.LinearLayout')[0]
        #第一级目录第一个的名称，并点击
        Layout.find_element_by_name(u'外饰配件').click()
        sleep(0.5)
        #第一级目录第二个
        Layout=listView1.find_elements_by_class_name('android.widget.LinearLayout')[1]
        #第一级目录第二个的名称，并点击
        Layout.find_element_by_name(u'内饰配件').click()
        sleep(0.5)
        #第一级目录第三个
        Layout=listView1.find_elements_by_class_name('android.widget.LinearLayout')[2]
        #第一级目录第三个的名称，并点击
        Layout.find_element_by_name(u'娱乐系统').click()
        sleep(0.5)
        #再次点击第一级目录第一个
        Layout=listView1.find_elements_by_class_name('android.widget.LinearLayout')[0]
        #再次点击第一级目录第一个的名称，并点击
        Layout.find_element_by_name(u'外饰配件').click()
        sleep(0.5)