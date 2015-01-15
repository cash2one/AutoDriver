# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'
#查询成功

import time
import unittest
from framework.core import testcase

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
    #预付款充值,导入方式充值CVS中只有一条记录140017充值1元，并查看充值付款界面是否有此记录，查看对应司机账户及公司押金账户是否有记录
    def test_import_prepay(self):

        self.driver.find_element_by_id('trade_prepay').click()
        self.driver.find_element_by_id('companyAccountId').find_elements_by_tag_name('option')[1].click()
        #勾选导入
        checkboxs = self.driver.find_elements_by_tag_name("input")
        print len(checkboxs)
        for a in checkboxs:
            if a.get_attribute('value')=='1':
                a.click()

        #定位上传按钮，添加本地文件（csv的路径：C:\Users\Administrator\Desktop\import.csv）
        self.driver.find_element_by_name('file').send_keys("C:\Users\Administrator\Desktop\import.csv")
        self.driver.find_element_by_id('import_memo').click()
        self.driver.find_element_by_id('import_memo').send_keys(u'自动化测试充值1元整')
        self.driver.find_element_by_id('btn_import').click()#点击导入,进入导入信息确认界面
        time.sleep(2)

        self.driver.find_element_by_id('btn_import_confirm').click()#点击确定，跳转导入结果界面
        time.sleep(2)

        #定位到导入结果界面，点击完成
        table4 = self.driver.find_element_by_id('import_result')
        table4.find_element_by_link_text('完成').click()#点击完成，跳转至充值付款界面

        #取出此条记录交易号，并检查付款方式为页面导入
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        tradeNo = trs[1].find_elements_by_tag_name('td')[2]
        tradeNo_text = tradeNo.get_attribute('title')
        operateType = trs[1].find_elements_by_tag_name('td')[6]
        operateType_text = operateType.get_attribute('title')
        print tradeNo_text,operateType_text
        self.assertTrue(u'页面导入' in operateType_text,'msg')

        #成功充值后，查询对应司机账户明细是否有记录
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('司机账户').click()
        time.sleep(2)
        self.driver.find_element_by_id('driverInfo').click()#输入查询条件140017
        self.driver.find_element_by_id('driverInfo').send_keys('140017')
        self.driver.find_element_by_id('query').click()#点击查询
        time.sleep(2)
        self.driver.find_element_by_id('view_driverAccount').click()#点击明细
        time.sleep(2)
        #查询此条交易记录的交易号tradeNo_text是否存在于司机明细列表中
        table1 = self.driver.find_element_by_id('list')
        trs1 = table1.find_elements_by_tag_name('tr')
        for i in range(1,len(trs1)-1):
            tds1 = trs1[i].find_elements_by_tag_name('td')[1]
            if  tds1.get_attribute('title') == tradeNo_text:
                print 'Ture',tds1.get_attribute('title')
            else:
                print 'False',tds1.get_attribute('title')
        time.sleep(2)

        #成功充值后，查询公司预付款账户明细是否有记录
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        trs2[17].find_element_by_id('detail').click()
        time.sleep(2)

        #查询此条交易记录的交易号tradeNo_text是否存在于公司预付款账户明细列表中
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        for i in range(1,len(trs1)-1):
            tds3 = trs3[i].find_elements_by_tag_name('td')[1]
            if  tds3.get_attribute('title') == tradeNo_text:
                print 'Ture',tds3.get_attribute('title')
            else:
                print 'False',tds3.get_attribute('title')
        time.sleep(2)

if __name__ =='__main__':
    unittest.main()