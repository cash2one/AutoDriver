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

    def test_case1(self):
        #调用activity方法
        self.activity()
        #点击主界面的电子说明书
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton1').click()
        sleep(0.5)
        #点击指示灯图标
        self.driver.find_element_by_id('cn.com.pathbook.carassist:id/imageButton_direction_light').click()
        sleep(0.5)
    def test_case2(self):
        self.test_case1()
        #查找整个view
        view=self.driver.find_element_by_id('cn.com.pathbook.carassist:id/gridview')
        #   # 点击第一个驾驶员安全带指示灯查询图标
        # self.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()
        # self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        # 点击第一个驾驶员安全带指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[0].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二个乘客安全带指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[1].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第三个安全气囊指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[2].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第四个充电系统指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[3].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
          #点击第五个故障指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[4].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第六个制动系统指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[5].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第七个电子驻车制动器指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[6].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第八个防抱死制动系统指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[7].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第九个牵引力关闭指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[8].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十个电子稳定控制装置指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[9].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十一个牵引力控制系统指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[10].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十二个轮胎气压指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[11].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十三个发动机机油压力指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[12].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十四个更换发动机机油指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[13].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十五个ECO指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[14].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十六个指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[15].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十七个燃油油位过低指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[16].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十八个加档灯指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[17].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第十九个尽快维修车辆指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[18].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十个超声波驻车传感器指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[19].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十一个发动机冷却液温度指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[20].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十二个安全指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[21].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十三个车门未关指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[22].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十四个巡航控制指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[23].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十五个远光灯开启指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[24].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十六个尾灯指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[25].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十七个前雾灯指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[26].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十八个后雾灯指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[27].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第二十九个自动前照灯调节指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[28].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第三十个全轮驱动指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[29].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第三十一个下坡控制系统指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[30].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第三十二个举升们未关指示灯查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[31].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        sleep(0.5)
        #点击第三十三个车辆提醒信息查询图标
        view.find_elements_by_class_name('android.widget.ImageView')[32].click()
        sleep(0.5)
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()