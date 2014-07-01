# coding=utf-8
__author__ = 'guguohai'


class Task():

    __state = False
    __testSuite={}

    def __init__(self,state,testSuite):
        self.__state = state
        self.__testSuite = testSuite


    def getState(self):
        return self.__state

    def setState(self):
        self.__state = True

    def getTestSuite(self):
        return self.__testSuite


    def finish(self):
        self.__state = False
        #所有测试用例的count-1
        for key in self.__testSuite:
            for k in self.__testSuite[key]:
                if self.__testSuite[key][k]<>0:
                    self.__testSuite[key][k]-=1






