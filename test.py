# coding=utf-8
__author__ = 'Administrator'

import sys
import time


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

if __name__ == "__main__":
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
    expect='aaa'
    actual='bbbb'
    expect_str = u'【期望结果】%s\r\n\r\n' % expect
    actual_str = u'【实际结果】\r\n%s' % actual
    c= expect_str + actual_str


    #rint  (u'\u4e5f\u6709').encode('utf-8')
    #a = '\u4e5f\u6709'
    a= c.encode('utf-8')
    cc='AssertionError: \u60a8\u7684\u7231\u8f66'
    #print eval("u"+'"'+a+'"')
    print eval("u"+'"'+cc+'"')