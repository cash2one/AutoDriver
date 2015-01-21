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
#     jira = JIRA(options={'server': 'http://192.168.3.11:8080'},basic_auth=('guguohai', 'guguohai'))
#
#     # projectKeys={'key': 'CI'}
#     # projectIds={'id': '10303'}
#     # issuetypeIds={'id': '3'}
#     # issuetypeNames={'name','Task'}
#     # print jira.createmeta(projectKeys,projectIds,issuetypeIds,issuetypeNames)
#     # issue_dict = {
#     #     'project': {'key': 'CI'},
#     #     'summary': 'New issue from jira-python',
#     #     'description': 'Look into this one',
#     #     'issuetype': {'name': 'Bug'},
#     # }
#     # new_issue = jira.create_issue(fields=issue_dict)
#     # print new_issue
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
        self.name='fff'

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
    #return inspect.getframeinfo(inspect.currentframe().f_back)[2]

def cccd():
    print get_current_function_name()


class ttes():
    def testtt(self):
        '''
        teststet
        :return:
        '''
        #print func_name()
        print 'ff::',get_current_function_name()
        d=dd()
        d.ccd()

def pyContent():

    file_object = open(PATH('./tesetcase/MyDemo/demo/test_order.pyc'))
    file_con = ''
    try:
        file_con = file_object.read()
    finally:
        file_object.close()
    return file_con

if __name__ == "__main__":
    print unicode('您的爱车', "utf-8")
    # from framework.util import http
    #
    # ja=http.TestJIRA()
    # ja.login()
    # time.sleep(5)
    #
    # ja.get_user()
    #
    # time.sleep(2)
    #
    # ja.create_issue()
