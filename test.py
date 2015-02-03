# coding=utf-8
__author__ = 'Administrator'

import sys
import os
import time
import json
import uuid
import re

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
    return inspect.stack()[1][1]  # [3]
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
    tree = [
        {
            u'订单管理': [
                {u'待处理订': [{'查询失败': []}]},
                {u'历史订单': [{'查询成功': []}]}
            ]
        },
        {u'客户管理': [
            {u'客户投诉': [
                {'回访': []}, {'审核': []}
            ]}
        ]
        }
    ]
    return tree


def PrintFrame():
    callerframerecord = inspect.stack()[1]  # 0 represents this line
    # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print info.filename  # __FILE__     -> Test.py
    print info.function  # __FUNCTION__ -> Main
    print info.lineno


def isHw(txt):
    txts = list(txt.lower())
    for i in range(0, len(txts) / 2):
        if cmp(txts[i], txts[-i - 1]) != 0:
            return False
    return True


def html2table(html, useid=False):
    trs = re.findall(r'<tr>.*?</tr>', html, re.DOTALL)
    rows = []
    for tr in trs:
        if useid:
            x = re.findall(r'>(?:<a [^<>]*id=(\w+)[^<>]*>)?([^<>]*)(?:</a>)?</td>', tr, re.DOTALL)
            x = map(lambda t: [t[0].strip(), t[1].strip()], x)
        else:
            x = re.findall(r'>([^<>]*)(?:</a>)?</td>', tr, re.DOTALL)
            x = map(lambda s: s.strip(), x)
        rows.append(x)
    return rows


def format_date(time_str):
    # return datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    return time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))


def get_localtime():
    # 将时间戳转化为localtime
    x = time.localtime(1317091800.0)
    return time.strftime('%Y-%m-%d %H:%M:%S', x)

def f_times(hour_):
    a = datetime.datetime.now().strftime('%Y-%m-%d '+hour_+':00:00.0')
    return time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S.%f'))

if __name__ == "__main__":
    # a = [[0]*8 for i in range(10)]
    #
    # print  os.path.realpath(__file__)

    # trs='<tr><td colspan="5"><p>ff1</p></td></tr><tr><td>ww1</td></tr>'
    # rr=re.compile(r'<td[^>]*(colspan="\d+")?>(<p>)?(\d+)(</p>)?</td>')
    # match = rr.findall(trs)
    #
    # print match
    #
    #
    # rr1=re.compile(r'<td.*?</td>')
    # match1 = rr1.findall(trs)
    #
    # print match1
    #
    # x = re.findall(r'>([^<>]*)(?:</p>)?</td>', trs, re.DOTALL)  # </p>
    # x = map(lambda s: s.strip(), x)
    # print x
    # #(r'>(?:<a [^<>]*colspan=(\w+)[^<>]*>)?([^<>]*)(?:</p>)?</td>', trs, re.DOTALL)#
    import datetime

    d1 = datetime.datetime.now()
    # d3 = d1 + datetime.timedelta(days=10)
    t3 = d1 - datetime.timedelta(minutes=30)

    #print datetime.datetime.now().strftime("%Y-%m-%d 09:00:00.0")


    for i in range(9, 18, 2):
        sp=f_times(str(i))-time.time()
        if sp<0:
            print sp
