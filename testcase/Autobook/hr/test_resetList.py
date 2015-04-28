# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()
        # 关闭浏览器
        # self.driver.close()

    #添加司机信息
    def test_adddriver(self):
        gltx=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').text
        self.assertTrue(u'司机管理' in gltx,u'对比信息不一致')
        self.driver.find_element_by_link_text(u'司机管理').click()
        addtx=self.driver.find_element_by_id('add').text
        self.assertTrue(u'添加' in addtx,u'对比信息不一致')
        self.driver.find_element_by_id('add').click()
        #  姓名
        self.driver.find_element_by_id('driverVo_name').send_keys(u'李美丽')
        nametx=self.driver.find_element_by_id('driverVo_name').get_attribute('value')
        self.assertTrue(u'李美丽' in nametx,u'对比信息不一致')
        #城市
        opts=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts:
            if opt.get_attribute('value')=='2':
                opt.click()
                # 判断是否点击
                self.assertTrue(opt.is_selected())
        #性别
        opts1=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts1:
            if opt.get_attribute('value')=='0':
                opt.click()
                self.assertTrue(opt.is_selected())
        #出生年月
        #年份
        opts2=self.driver.find_element_by_id('year').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts2:
            if opt.get_attribute('value')=='1999':
                opt.click()
                self.assertTrue(opt.is_selected())
        #月份
        opts3=self.driver.find_element_by_id('month').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts3:
            if opt.get_attribute('value')=='10':
                opt.click()
                self.assertTrue(opt.is_selected())
        #婚育
        opts4=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts4:
            if opt.get_attribute('value')=='0':
                opt.click()
                self.assertTrue(opt.is_selected())
        #籍贯
        opts5=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts5:
            if opt.get_attribute('value')=='3':
                opt.click()
                self.assertTrue(opt.is_selected())
        #身份证号码
        self.driver.find_element_by_id('driverVo_card').send_keys(u'61232119991020111X')
        cardtx=self.driver.find_element_by_id('driverVo_card').get_attribute('value')
        self.assertTrue(u'61232119991020111X' in cardtx,u'对比信息不一致')
        #驾驶证号码
        self.driver.find_element_by_id('detailVo_licenseNum').send_keys(u'61232119991020111X')
        licenseNumtx=self.driver.find_element_by_id('detailVo_licenseNum').get_attribute('value')
        self.assertTrue(u'61232119991020111X' in licenseNumtx,u'对比信息不一致')
        #驾驶档案编号
        self.driver.find_element_by_id('detailVo_licenseNo').send_keys('10000101')
        licenseNotx=self.driver.find_element_by_id('detailVo_licenseNo').get_attribute('value')
        self.assertTrue(u'10000101' in licenseNotx,u'对比信息不一致')
        #驾照申领日期
        js = '$(\'input[id=detailVo_licencetime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        #清除已有数据
        self.driver.find_element_by_id('detailVo_licencetime').clear()
        #输入内容
        self.driver.find_element_by_id('detailVo_licencetime').send_keys('2015-01-14')
        licencetimetx=self.driver.find_element_by_id('detailVo_licencetime').get_attribute('value')
        self.assertTrue(u'2015-01-14' in licencetimetx,u'对比信息不一致')
        #本人电话
        self.driver.find_element_by_id('driverVo_phone').send_keys('13122223333')
        phonetx=self.driver.find_element_by_id('driverVo_phone').get_attribute('value')
        self.assertTrue(u'13122223333' in phonetx,u'对比信息不一致')
        #imsi
        self.driver.find_element_by_id('driverVo_imsi').send_keys('460001234598765')
        imsitx=self.driver.find_element_by_id('driverVo_imsi').get_attribute('value')
        self.assertTrue(u'460001234598765' in imsitx,u'对比信息不一致')
        #上传头像
        self.driver.find_element_by_id('file').send_keys('E:\\image1.png')
        #邮箱
        self.driver.find_element_by_id('driverVo_email').send_keys('abcd123@163.com')
        emailtx=self.driver.find_element_by_id('driverVo_email').get_attribute('value')
        self.assertTrue(u'abcd123@163.com' in emailtx,u'对比信息不一致')
        #户口地址
        self.driver.find_element_by_id('detailVo_oldAddress').send_keys(u'北京市朝阳区霄云路甲A区32号')
        oldAddresstx=self.driver.find_element_by_id('detailVo_oldAddress').get_attribute('value')
        self.assertTrue(u'北京市朝阳区霄云路甲A区32号' in oldAddresstx,u'对比信息不一致')
        #户口邮编
        self.driver.find_element_by_id('detailVo_oldPostcode').send_keys('100027')
        oldPostcodetx=self.driver.find_element_by_id('detailVo_oldPostcode').get_attribute('value')
        self.assertTrue(u'100027' in oldPostcodetx,u'对比信息不一致')
        #现地址
        self.driver.find_element_by_id('detailVo_newAddress').send_keys(u'上海市闵行区万源路2158号')
        newAddresstx=self.driver.find_element_by_id('detailVo_newAddress').get_attribute('value')
        self.assertTrue(u'上海市闵行区万源路2158号' in newAddresstx,u'对比信息不一致')
        #现住邮编
        self.driver.find_element_by_id('detailVo_newPostcode').send_keys('201101')
        newPostcodetx=self.driver.find_element_by_id('detailVo_newPostcode').get_attribute('value')
        self.assertTrue(u'201101' in newPostcodetx,u'对比信息不一致')
        #民族
        self.driver.find_element_by_id('detailVo_nation').send_keys(u'汉')
        nationtx=self.driver.find_element_by_id('detailVo_nation').get_attribute('value')
        self.assertTrue(u'汉' in nationtx,u'对比信息不一致')
        #身高
        self.driver.find_element_by_id('detailVo_height').send_keys('165')
        heighttx=self.driver.find_element_by_id('detailVo_height').get_attribute('value')
        self.assertTrue(u'165' in heighttx,u'对比信息不一致')
        #户籍类别
        opts6=self.driver.find_element_by_id('container_placeType').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in opts6:
            if opt.get_attribute('value')=='1':
                opt.click()
                self.assertTrue(opt.is_selected())
        #体重
        self.driver.find_element_by_id('detailVo_weight').send_keys('50')
        weighttx=self.driver.find_element_by_id('detailVo_weight').get_attribute('value')
        self.assertTrue(u'50' in weighttx,u'对比信息不一致')
        #电脑水平
        opts7=self.driver.find_element_by_id('detailVo_computerLevel').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts7:
            if opt.get_attribute('value')=='2':
                opt.click()
                self.assertTrue(opt.is_selected())
        #英语水平
        opts7=self.driver.find_element_by_id('detailVo_englishLevel').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts7:
            if opt.get_attribute('value')=='2':
                opt.click()
                self.assertTrue(opt.is_selected())
        #学历
        opts8=self.driver.find_element_by_id('detailVo_education').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts8:
            if opt.get_attribute('value')=='2':
                opt.click()
                self.assertTrue(opt.is_selected())
        #专业
        self.driver.find_element_by_id('detailVo_major').send_keys(u'旅游管理')
        majortx=self.driver.find_element_by_id('detailVo_major').get_attribute('value')
        self.assertTrue(u'旅游管理' in majortx,u'对比信息不一致')
        #健康状况
        self.driver.find_element_by_id('detailVo_bodyState').send_keys(u'健康')
        bodyStatetx=self.driver.find_element_by_id('detailVo_bodyState').get_attribute('value')
        self.assertTrue(u'健康' in bodyStatetx,u'对比信息不一致')
        #准驾车型
        opts9=self.driver.find_element_by_id('driverVo_licenseType').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts9:
            if opt.get_attribute('value')=='1':
                opt.click()
                self.assertTrue(opt.is_selected())
        # 熟练驾驶车型
        opts10=self.driver.find_element_by_id('container_carType').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in opts10:
            if opt.get_attribute('value')=='1':
                opt.click()
                self.assertTrue(opt.is_selected())
        # 熟练驾驶车型全选
        self.driver.find_element_by_id('carType_CheckAll').click()
        # 驾龄
        self.driver.find_element_by_id('driverVo_drivingAge').send_keys('5')
        Agetx=self.driver.find_element_by_id('driverVo_drivingAge').get_attribute('value')
        self.assertTrue(u'5' in Agetx,u'对比信息不一致')
        # 设备领用
        opts11=self.driver.find_element_by_id('container_equipment').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in opts11:
            if opt.get_attribute('value')=='1':
                opt.click()
                self.assertTrue(opt.is_selected())
        # 设备领用全选
        self.driver.find_element_by_id('equipment_CheckAll').click()
        # 紧急联系人姓名
        self.driver.find_element_by_id('detailVo_urgencyName').send_keys(u'胡英俊')
        urgencyNametx=self.driver.find_element_by_id('detailVo_urgencyName').get_attribute('value')
        self.assertTrue(u'胡英俊' in urgencyNametx,u'对比信息不一致')
        # 紧急联系人电话
        self.driver.find_element_by_id('detailVo_urgencyTel').send_keys('18722222222')
        urgencyTeltx=self.driver.find_element_by_id('detailVo_urgencyTel').get_attribute('value')
        self.assertTrue(u'18722222222' in urgencyTeltx,u'对比信息不一致')
        # 关系
        opts12=self.driver.find_element_by_id('detailVo_urgencyRelation').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts12:
            if opt.get_attribute('value')=='1':
                opt.click()
                self.assertTrue(opt.is_selected())
        #代驾经验
        self.driver.find_element_by_id('detailVo_drivingExperience').click()
        self.driver.find_element_by_id('detailVo_drivingExperience').send_keys(u'驾驶经验丰富，年轻、沟通能力强。熟悉道路及各种中高档次各款车型。')
        time.sleep(1)
        Experiencetx=self.driver.find_element_by_id('detailVo_drivingExperience').get_attribute('value')
        self.assertTrue(u'驾驶经验丰富，年轻、沟通能力强。熟悉道路及各种中高档次各款车型。' in Experiencetx,u'对比信息不一致')

    def test_reset(self):
        # 重置
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/a[2]').click()
        time.sleep(3)
        #判断姓名
        nametx=self.driver.find_element_by_id('driverVo_name').text
        self.assertTrue(nametx=='')
        #判断城市
        citytx=self.driver.find_element_by_id('driverVo_city').find_elements_by_tag_name('option')
        print citytx
        for opt in citytx:
            if opt.get_attribute('text')==u'请选择':
                print u'重置成功....'
        #判断性别
        citytx=self.driver.find_element_by_id('driverVo_sex').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in citytx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'

        #判断出生年月
        yeartx=self.driver.find_element_by_id('year').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in yeartx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        monthtx=self.driver.find_element_by_id('month').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in monthtx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断婚育
        marriagetx=self.driver.find_element_by_id('detailVo_marriage').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in marriagetx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断籍贯
        provincetx=self.driver.find_element_by_id('driverVo_province').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in provincetx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断身份证号码
        cardtx=self.driver.find_element_by_id('driverVo_card').text
        self.assertTrue(cardtx=='')
        #判断驾驶证
        numtx=self.driver.find_element_by_id('detailVo_licenseNum').text
        self.assertTrue(numtx=='')
        #判断档案编号
        notx=self.driver.find_element_by_id('detailVo_licenseNo').text
        self.assertTrue(notx=='')
        #判断申领时间
        timetx=self.driver.find_element_by_id('detailVo_licencetime').text
        self.assertTrue(timetx=='')
        #判断本人电话
        phonetx=self.driver.find_element_by_id('driverVo_name').text
        self.assertTrue(phonetx=='')
        #判断imsi
        imsitx=self.driver.find_element_by_id('driverVo_imsi').text
        self.assertTrue(imsitx=='')
         #判断邮箱
        emailtx=self.driver.find_element_by_id('driverVo_email').text
        self.assertTrue(emailtx=='')
        #判断户口地址
        oldAddrestx=self.driver.find_element_by_id('detailVo_oldAddress').text
        self.assertTrue(oldAddrestx=='')
         #判断户口邮编
        oldPostcodetx=self.driver.find_element_by_id('detailVo_oldPostcode').text
        self.assertTrue(oldPostcodetx=='')
        #判断现居地址
        newAddresstx=self.driver.find_element_by_id('detailVo_newAddress').text
        self.assertTrue(newAddresstx=='')
        #判断现居邮编
        newPostcodetx=self.driver.find_element_by_id('detailVo_newPostcode').text
        self.assertTrue(newPostcodetx=='')
        #判断民族
        nationtx=self.driver.find_element_by_id('detailVo_nation').text
        self.assertTrue(nationtx=='')
        #判断身高
        heighttx=self.driver.find_element_by_id('detailVo_height').text
        self.assertTrue(heighttx=='')
        #判断户籍类别
        provincetx=self.driver.find_element_by_id('container_placeType').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in provincetx:
            if opt.get_attribute('value')=='1':
                 print u'重置成功....'
        #判断体重
        weighttx=self.driver.find_element_by_id('detailVo_weight').text
        self.assertTrue(weighttx=='')
        #判断电脑水平
        computertx=self.driver.find_element_by_id('detailVo_computerLevel').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in computertx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断英语水平
        englishtx=self.driver.find_element_by_id('detailVo_englishLevel').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in englishtx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断学历
        educationtx=self.driver.find_element_by_id('detailVo_education').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in educationtx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断专业
        majortx=self.driver.find_element_by_id('detailVo_major').text
        self.assertTrue(majortx=='')
        #判断健康状况
        Statetx=self.driver.find_element_by_id('detailVo_bodyState').text
        self.assertTrue(Statetx=='')
        #判断准驾车型
        Typetx=self.driver.find_element_by_id('driverVo_licenseType').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in Typetx:
            if opt.get_attribute('text')==u'请选择':
                 print u'重置成功....'
        #判断驾龄
        Agetx=self.driver.find_element_by_id('driverVo_drivingAge').text
        self.assertTrue(Agetx=='')
        #判断熟练驾车型
        cartx=self.driver.find_element_by_id('container_carType').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in cartx:
            if opt.get_attribute('value')=='':
               print u'重置成功....'
        #判断设备领用
        equipmenttx=self.driver.find_element_by_id('container_equipment').find_elements_by_tag_name('input')
        time.sleep(1)
        for opt in equipmenttx:
            if opt.get_attribute('value')=='':
               print u'重置成功....'
        #判断紧急联系人
        urgencyNametx=self.driver.find_element_by_id('detailVo_urgencyName').text
        self.assertTrue(urgencyNametx=='')
        #判断电话
        urgencyTeltx=self.driver.find_element_by_id('detailVo_urgencyTel').text
        self.assertTrue(urgencyTeltx=='')
        #判断关系
        Relationtx=self.driver.find_element_by_id('detailVo_urgencyRelation').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in Relationtx:
            if opt.get_attribute('text')==u'请选择':
               print u'重置成功....'

        #判断电话
        Experiencetx=self.driver.find_element_by_id('detailVo_drivingExperience').text
        self.assertTrue(Experiencetx=='')
        # #添加
        # self.driver.find_element_by_id('btn_add').click()
        #列表
        lbtx=self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/a[3]').text
        self.assertTrue(u'司机列表' in lbtx)
        self.driver.find_element_by_link_text(u'司机列表').click()
        print self.driver.title
        self.assertTrue(u'司机管理/司机列表' in self.driver.title,u'界面跳转错误')


