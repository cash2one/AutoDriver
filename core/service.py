__author__ = 'Administrator'

import threading
import time

class Service(threading.Thread):
    def __init__(self, num, interval,testCaseDict):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
        self.cases = testCaseDict

    def run(self):
        while not self.thread_stop:
            print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
            print self.cases
            time.sleep(self.interval)

    def stop(self):
        self.thread_stop = True