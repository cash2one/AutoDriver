# coding=utf-8
__author__ = 'guohai@live.com'
#任务基类，所有case运行都通过继承实现


class TaskBase(object):

    case_id = 0
    case_name = ''
    case_loop = 0

    def __init__(self,testCase):
        pass

    def sendMsg(self,case_id,state):
        pass

    def start(self):
        print 'start....'

    def finish(self):
        print 'finish...'

    def stop(self):
        print 'stop...'

