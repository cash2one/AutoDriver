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
    a=': fwfefe'
    print a[1:].strip()