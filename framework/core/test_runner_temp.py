# coding=utf-8
__author__ = 'Administrator'

import sys
import datetime
import test_result_temp

class TestRunner():

    def __init__(self,task=None):
        self.task = task
        self.startTime = datetime.datetime.now()

    def run(self, test):
        result = test_result_temp.NewTestResult()
        test(result)
        self.stopTime = datetime.datetime.now()
        self.task.finish()

        #print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)
        return result
