# coding=utf-8
__author__ = 'guguohai@outlook.com'

import sys
import unittest
import StringIO
import datetime
import re
#from PyQt4 import QtCore

from framework.core import box
#from framework.util import pyqt


STATUS = {
    0: 'pass',
    1: 'fail',
    2: 'error',
}


class NewTestResult(unittest.TestResult):
    def __init__(self, dbm=None, product_info=None):#, ui=None):
        unittest.TestResult.__init__(self)
        self.dbm = dbm
        self.product_info = product_info
        #self.ui = ui
        self.test_user = box.jira.userName
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

        value = str(test)
        s = value.find('(')
        e = value.find('.')

        ExecuteResult = STATUS[self.currentStatus]
        Executor = self.test_user
        Owner = ''
        ResultDesc = self.getAssertResult().decode("unicode-escape")
        IsEnable = 1
        LogFile = ''
        ExecuteDT = datetime.datetime.now()
        ProductName = value[s + 1:e + 1] + value[0:s]
        ProductTypeName = ''
        TestCase_Id = 1
        Task_Id = 1

        data = (ExecuteResult, Executor, Owner, ResultDesc, IsEnable, LogFile, ExecuteDT, ProductName, ProductTypeName,
                TestCase_Id, Task_Id)

        sql = "INSERT INTO Result values (NULL,?,?,?,?,?,?,?,?,?,?,?)"
        if self.dbm != None:
            self.dbm.insert_value(sql, data)
        # if self.ui != None:
        #     self.ui.emit(QtCore.SIGNAL("finish_case"), data)
        #pyqt.finish_case(self.ui,data)

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
        assert_str = ''
        for ex in self.excepts:
            if ex in result_desc:  # AssertionError:
                ex_idx = result_desc.find(ex) + len(ex)
                r_desc = result_desc[ex_idx:len(result_desc)]
                assert_str = r_desc[1:].strip()
                break

        return assert_str


        # ex_str = r'(?<=%s:).*' % ex
        # match = re.compile(ex_str).search(result_desc)
        # if match:
        # return ex + ':' + match.group()
        # else:
        # return ''


# 获取exceptions 所有Error的类名
def getExcepts():
    # excepts = []
    __import__('exceptions')
    m = sys.modules['exceptions']
    attstr = dir(m)
    return attstr

    # for strr in attstr:
    # att = str(getattr(m, strr))
    # #print att
    # pattern = re.compile(r'(?<=exceptions.).*Error')
    # match = pattern.search(att)
    # if match:
    # excepts.append(match.group())
    # return excepts
