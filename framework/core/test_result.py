# coding=utf-8
__author__ = 'guguohai@outlook.com'

import sys
import unittest
import StringIO
import time
import datetime
import re
from framework.core import the

STATUS = {
0: 'pass',
1: 'fail',
2: 'error',
}

class NewTestResult(unittest.TestResult):
    def __init__(self,dbm=None,product_info=None):
        unittest.TestResult.__init__(self)
        self.dbm = dbm
        self.product_info = product_info
        self.testUser = the.settings['user']['name']
        self.currentStatus = 0

        self.result = []

        self.fail_str = ''
        self.error_str = ''
        self.excepts = getExcepts()


    def startTest(self, test):
        unittest.TestResult.startTest(self, test)
        self.outputBuffer = StringIO.StringIO()

        self.currentStatus = 0

        self.fail_str = ''
        self.error_str = ''


    def complete_output(self):
        return self.outputBuffer.getvalue()


    def stopTest(self, test):
        self.complete_output()
        _testcase = str(test)

        result_desc = self.getAssertResult()
        startDT = datetime.datetime.now()
        #data1 = [(_testcase,_count,self.currentSuccess,self.currentFail,self.currentError,_update_time,_detail)]
        #自动化脚本里没有task，默认id为1
        data = (STATUS[self.currentStatus],self.testUser,result_desc,1,'',startDT,'Product_name','Product_TYPE',1,1,1)

        sql = "INSERT INTO Result values (NULL,?,?,?,?,?,?,?,?,?,?,?)"
        self.dbm.insert_value(sql,data)


    def addSuccess(self, test):
        unittest.TestResult.addSuccess(self, test)
        output = self.complete_output()

        self.result.append((0, test, output, ''))
        self.currentStatus = 0
        sys.stderr.write('.')

    def addFailure(self, test, err):
        unittest.TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()

        self.result.append((1, test, output, _exc_str))
        self.fail_str = _exc_str

        self.currentStatus = 1
        sys.stderr.write('F')

    def addError(self, test, err):
        unittest.TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()

        self.result.append((2, test, output, _exc_str))

        self.error_str = _exc_str

        self.currentStatus = 2
        sys.stderr.write('E')

    def getAssertResult(self):
        result_desc = ''
        if self.fail_str.strip() != '':
            result_desc = self.fail_str
        elif self.error_str.strip() != '':
            result_desc = self.error_str

        print result_desc

        for ex in self.excepts:
            ex_str = r'(?<=%s:).*' % ex
            match = re.compile(ex_str).search(result_desc)
            if match:
                return ex+ ':' + match.group()
            else:
                return ''


#获取exceptions 所有Error的类名
def getExcepts():
    excepts = []
    __import__('exceptions')
    m = sys.modules['exceptions']
    attstr = dir(m)
    for strr in attstr:
        att = str(getattr(m,strr))
        pattern = re.compile(r'(?<=exceptions.).*Error')
        match = pattern.search(att)
        if match:
            excepts.append(match.group())
    return excepts
