# coding=utf-8
__author__ = 'guguohai@outlook.com'

import sys
import datetime
import test_result

class TestRunner():

    def __init__(self,db=None,task=None):
        self.dbm = db
        self.task = task
        self.startTime = datetime.datetime.now()

    def run(self, test):
        result = test_result.NewTestResult(self.dbm)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.dbm.close_db()
        self.task.finish()

        print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)
        return result
