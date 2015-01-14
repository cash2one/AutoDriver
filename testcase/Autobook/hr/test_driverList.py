# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
import unittest
from framework.core import idriver_web


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        #登录平台
        self.driver.login()

    def tearDown(self):
         #返回首页
        # self.driver.switch_to_home()
        time.sleep(5)
         #关闭浏览器
        # self.driver.close()
    #添加司机信息
    def test_adddriver(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        self.driver.find_element_by_id('add').click()
        #  姓名
        self.driver.find_element_by_id('driverVo_name').send_keys(u'李美丽')
        #城市
        opts=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts:
            if opt.get_attribute('value')=='2':
                opt.click()
        #性别
        opts1=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts1:
            if opt.get_attribute('value')=='0':
                opt.click()
        #出生年月
        #年份
        opts2=self.driver.find_element_by_id('year').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts2:
            if opt.get_attribute('value')=='1999':
                opt.click()
        #月份
        opts3=self.driver.find_element_by_id('month').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts3:
            if opt.get_attribute('value')=='10':
                opt.click()
        #婚育
        opts4=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts4:
            if opt.get_attribute('value')=='0':
                opt.click()
        #籍贯
        opts5=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts5:
            if opt.get_attribute('value')=='3':
                opt.click()
        #身份证号码
        self.driver.find_element_by_id('driverVo_card').send_keys(u'61232119991020111X')
        #驾驶证号码
        self.driver.find_element_by_id('detailVo_licenseNum').send_keys(u'61232119991020111X')
        #驾驶档案编号
        self.driver.find_element_by_id('detailVo_licenseNo').send_keys('10000101')
        #驾照申领日期
        js = '$(\'input[id=detailVo_licencetime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        #清除已有数据
        self.driver.find_element_by_id('detailVo_licencetime').clear()
        #输入内容
        self.driver.find_element_by_id('detailVo_licencetime').send_keys('2015-01-06')
        #本人电话
        self.driver.find_element_by_id('driverVo_phone').send_keys('13122223333')
        #imsi
        self.driver.find_element_by_id('driverVo_imsi').send_keys('460001234598765')
        #上传头像
        self.driver.find_element_by_id('file').send_keys('E:\\image1.png')
        #邮箱
        self.driver.find_element_by_id('driverVo_email').send_keys('abcd123@163.com')
        #户口地址
        self.driver.find_element_by_id('detailVo_oldAddress').send_keys(u'北京市朝阳区霄云路甲A区32号')
        #户口邮编
        self.driver.find_element_by_id('detailVo_oldPostcode').send_keys('100027')
        #现地址
        self.driver.find_element_by_id('detailVo_newAddress').send_keys(u'上海市闵行区万源路2158号')
        #现住邮编
        self.driver.find_element_by_id('detailVo_newPostcode').send_keys('201101')
        #民族
        self.driver.find_element_by_id('detailVo_nation').send_keys(u'汉')
        #身高
        self.driver.find_element_by_id('detailVo_height').send_keys('165')
        #户籍类别
        opts6=self.driver.find_element_by_id('container_placeType').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in opts6:
            if opt.get_attribute('value')=='1':
                opt.click()
        #体重
        self.driver.find_element_by_id('detailVo_weight').send_keys('50')
        #电脑水平
        opts7=self.driver.find_element_by_id('detailVo_computerLevel').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts7:
            if opt.get_attribute('value')=='2':
                opt.click()
        #英语水平
        opts7=self.driver.find_element_by_id('detailVo_englishLevel').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts7:
            if opt.get_attribute('value')=='2':
                opt.click()
        #学历
        opts8=self.driver.find_element_by_id('detailVo_education').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts8:
            if opt.get_attribute('value')=='2':
                opt.click()
        #专业
        self.driver.find_element_by_id('detailVo_major').send_keys(u'旅游管理')
        #健康状况
        self.driver.find_element_by_id('detailVo_bodyState').send_keys(u'健康')
        #准驾车型
        opts9=self.driver.find_element_by_id('driverVo_licenseType').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts9:
            if opt.get_attribute('value')=='1':
                opt.click()
        # 熟练驾驶车型
        opts10=self.driver.find_element_by_id('container_carType').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in opts10:
            if opt.get_attribute('value')=='1':
                opt.click()
        # 熟练驾驶车型全选
        self.driver.find_element_by_id('carType_CheckAll').click()
        # 驾龄
        self.driver.find_element_by_id('driverVo_drivingAge').send_keys('5')
        # 设备领用
        opts11=self.driver.find_element_by_id('container_equipment').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in opts11:
            if opt.get_attribute('value')=='1':
                opt.click()
        # 设备领用全选
        self.driver.find_element_by_id('equipment_CheckAll').click()
        # 紧急联系人姓名
        self.driver.find_element_by_id('detailVo_urgencyName').send_keys(u'胡英俊')
        # 紧急联系人电话
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys('18722222222')
        # 关系
        opts12=self.driver.find_element_by_id('detailVo_urgencyRelation').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts12:
            if opt.get_attribute('value')=='1':
                opt.click()
        #代价经验
        self.driver.find_element_by_id('detailVo_drivingExperience').click()
        self.driver.find_element_by_id('detailVo_drivingExperience').send_keys(u'驾驶经验丰富，年轻、沟通能力强。熟悉道路及各种中高档次各款车型。')
        time.sleep(5)
        # 重置
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/a[2]').click()
        time.sleep(5)
        # #添加
        # self.driver.find_element_by_id('btn_add').click()
        #列表
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/a[3]').click()