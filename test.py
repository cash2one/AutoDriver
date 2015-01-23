# coding=utf-8
__author__ = 'Administrator'

import sys
import os
import time
import json
import uuid

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def add_path():
    import webbrowser

    webbrowser.open('http://www.baidu.com')

# def jiraa():
# from jira.client import JIRA
# jira = JIRA(options={'server': 'http://192.168.3.11:8080'},basic_auth=('guguohai', 'guguohai'))
#
# # projectKeys={'key': 'CI'}
# # projectIds={'id': '10303'}
# # issuetypeIds={'id': '3'}
# # issuetypeNames={'name','Task'}
# # print jira.createmeta(projectKeys,projectIds,issuetypeIds,issuetypeNames)
# # issue_dict = {
# #     'project': {'key': 'CI'},
# #     'summary': 'New issue from jira-python',
# #     'description': 'Look into this one',
# #     'issuetype': {'name': 'Bug'},
# # }
# # new_issue = jira.create_issue(fields=issue_dict)
# # print new_issue
import inspect


class dd():
    '''
    gweg wwe egwge w
    '''

    def __init__(self):
        '''
        fwege
        :return:
        '''
        self.name = 'fff'

    def ccd(self):
        '''
        geeeee
        :return:
        '''
        print self.__class__.__name__
        print self.__doc__


def func_name():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    return f.f_code.co_name  # (f.f_code.co_name, f.f_lineno)


def get_current_function_name():
    return inspect.stack()[1][3]
    # return inspect.getframeinfo(inspect.currentframe().f_back)[2]


def cccd():
    print get_current_function_name()


class ttes():
    def testtt(self):
        '''
        teststet
        :return:
        '''
        # print func_name()
        print 'ff::', get_current_function_name()
        d = dd()
        d.ccd()


def cats():
    # cat = [u'订单管理\待处理订单\查询失败', u'订单管理\历史订单\查询成功', u'客户管理\客户投诉\回访', u'客户管理\客户投诉\审核']
    cat = [u'order\\pending\\findFail\\fwgweg\\eeee', u'order\\history\\findSuccess', u'customer\\complain\\vaisit',
           u'customer\\complain\Auditing']
    cat = list(set(cat))

    tree = [
        {
            u'订单管理':
                [
                    {
                        u'待处理订': [u'查询失败']
                    },
                    {
                        u'历史订单': [u'查询成功']
                    }
                ]
        },
        {u'客户管理':
             [
                 {
                     u'客户投诉': ['回访', '审核']
                 },
                 {
                     u'客户xx': ['oo', 'cc']
                 }
             ]
        }
    ]
    return cat



def PrintFrame():
    callerframerecord = inspect.stack()[1]  # 0 represents this line
    # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print info.filename  # __FILE__     -> Test.py
    print info.function  # __FUNCTION__ -> Main
    print info.lineno


def gg():
    PrintFrame()


if __name__ == "__main__":
    # a = [[0]*8 for i in range(10)]
    #
    # print  os.path.realpath(__file__)
    from framework.util import strs
    print json.dumps(strs.path_to_tree((cats())))

