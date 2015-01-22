# coding=utf-8
__author__ = 'Administrator'

import sys
import os
import time

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
    print cat
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
                 }
             ]
        }
    ]
    return cat


def load_tree(cat):
    trees = []
    for ca in cat:
        t = tuple(ca.split('\\'))

        t_tup = ()
        for i in range(0, len(t) - 1):
            di = {}
            di[t[i]] = t[i + 1]
            t_tup += (di,)

        print t_tup

        t_dict = {}
        for m in range(0, len(t_tup) - 1):
            if t_tup[m].values()[0] == t_tup[m + 1].keys()[0]:
                t_dict[t_tup[m].values()[0]] = t_tup[m + 1]
        print t_dict
        trees.append(t_dict)

    print trees


def scan_path(path_str, i):
    di = {}
    di[path_str[i]] = path_str[i + 1]
    return di
    # t_dict[path_str[i]] = di



    # for i in range(0,len(cats)):


if __name__ == "__main__":
    # a = [[0]*8 for i in range(10)]
    print load_tree(cats())

