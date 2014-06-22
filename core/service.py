# coding=utf-8
__author__ = 'guohai@live.com'

import os
import sys
import threading
import time
from taskManager import TaskManager as tm


class Service:

    CASE_STATUS_FINISH = 'finish'
    CASE_STATUS_RUNNING = 'running'

    mid = ''

    def __init__(self, case_id):
        self.mid = case_id

    #接收系统消息
    def receive(self, case_id, case_state):
        if case_state == self.CASE_STATUS_FINISH:
            case_id -= case_id
            tm.find_case(case_id)


            print 'finish'

    def monitor(self, interval):
        while not self.thread_stop:
            print 'Thread Object---'
            time.sleep(interval)


def test():
    thread1 = Service()
    thread1.start()
    return

if __name__ == '__main__':
    test()