# coding=utf-8

__author__ = 'Administrator'

import sys
import unittest
import StringIO
import time
import outputRedirector

stdout_redirector = outputRedirector.OutputRedirector(sys.stdout)
stderr_redirector = outputRedirector.OutputRedirector(sys.stderr)

class NewTestResult(unittest.TestResult):
    def __init__(self, verbosity=1,dbm=None):
        unittest.TestResult.__init__(self)
        self.dbm=dbm
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.result = []


    def startTest(self, test):
        unittest.TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = StringIO.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector


    def complete_output(self):
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()


    def stopTest(self, test):
        self.complete_output()
        timestr=time.ctime()
        data = [(timestr, u'登陆火星计划不靠谱'),
                 (timestr, u'数据库表测试')]

        sql = "INSERT INTO module values (NULL , ?, ?)"
        self.dbm.insert_values(sql,data)

    def addSuccess(self, test):
        self.success_count += 1
        unittest.TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        unittest.TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        unittest.TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')