# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

#初始化项目时的字典统一key
PRODUCT='pathbook_product'

driver = 'idriver.android.driver'
driver_robot = 'idriver.android.driver_robot'
customer = 'idriver.android.customer'
customer_robot = 'idriver.android.customer_robot'
ir='emanual.web.ir'

SEP = '|'
FLOW_NAME = 'flow'
INTERFACE_FOLDER = 'autobook_interface'
CUSTOMER_LOGIN = '/service/customerService/login'
DRIVER_LOGIN = '/service/driverService/login'
DRIVER_SERVICE = 'service/driverService'
CUSTOMER_SERVICE = 'service/customerService'
COMMON_SERVICE = 'service/commonService'

CORE_PATH_CONFIG = '../../config.ini'

EXCEL_HEADER = {
'no':u'用例编号',
'cat':u'分类',
'desc':u'用例描述',
'exp':u'期望结果',
'script':u'用例脚本',
'loop':u'执行次数'
}

TOKEN_NO = '{{tokenNo}}'
PHONE = '{{phone}}'
PMID = '{{pmId}}'


INTERFACE_HEADER = r'''# coding=utf-8

import unittest
from framework.core import interface

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
'''

INTERFACE_FLOW = r'''
    def test_interface_%(no)s(self):
        desc = interface.toList(u'%(desc)s')
        exp = interface.toList(u'%(exp)s')
        for i in range(0,len(desc)):
            interface.assertResult(self,desc[i],exp[i])
'''

INTERFACE_NON_FLOW = r'''
    def test_interface_%(no)s(self):
        desc = u'%(desc)s'
        exp = u'%(exp)s'
        interface.assertResult(self,desc,exp)
'''