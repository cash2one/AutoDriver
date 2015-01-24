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
    cat = [u'订单管理\待处理订单\查询失败', u'订单管理\历史订单\查询成功', u'客户管理\客户投诉\回访', u'客户管理\客户投诉\审核']
    cat = list(set(cat))

    tree = [
        {
            u'订单管理':
                [
                    {
                        u'待处理订': [{'查询失败': []}]
                    },
                    {
                        u'历史订单': [{'查询成功': []}]
                    }
                ]
        },
        {u'客户管理':
             [
                 {
                     u'客户投诉': [{'回访': []}, {'审核': []}]
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


def walk_tree(nodes):
    new_list = []
    left_list = []
    yq = []
    parents = []
    for i in range(0, len(nodes)):
        if nodes[i]['parent_id'] == None:
            parents.append(nodes[i])


    for i in range(0, len(nodes)):
        for p in parents:
            p_s = {p['name']: []}
            if p['self_id'] == nodes[i]['parent_id']:
                p_s[p['name']].append({nodes[i]['name']: []})
                yq.append(i)

            if not i in yq:
                p_s['name'] = nodes[i]['name']
                p_s['self_id'] = nodes[i]['self_id']
                p_s['parent_id'] = nodes[i]['parent_id']

                new_list.append(p_s)

    # for i in range(0, len(nodes)):
    #
    #     self_s = {nodes[i]['name']: [], 'parent_id': ''}
    #     for n in range(i + 1, len(nodes)):
    #
    #         # 把子都找出来
    #         if nodes[i]['self_id'] == nodes[n]['parent_id']:
    #             self_s[nodes[i]['name']].append({nodes[n]['name']: []})
    #             yq.append(n)

                # for n in range(i + 1, len(nodes)):
                # parent_s = {nodes[n]['name']: [], 'parent_id': ''}
                #     if nodes[i]['parent_id'] == nodes[n]['self_id']:
                #         parent_s[nodes[n]['name']].append(self_s)
                #         yq.append(n)

                # 后面的子 没找出来

        # if not i in yq:
        #     self_s['name'] = nodes[i]['name']
        #     self_s['self_id'] = nodes[i]['self_id']
        #     self_s['parent_id'] = nodes[i]['parent_id']
        #
        #     new_list.append(self_s)






            # if self_s['parent_id'] == None:


            # else:
            # left_list.append(self_s)

            # for new in new_list:
            # if new['parent_id']!=None:
            # walk_tree(new_list)
            #
            # if len(n_list) > 0:
            # new_list.append(n_list)

    return new_list, left_list


def ddd(nodes):
    # new_nodes = walk_tree(nodes)
    for node in nodes:
        if node['parent_id'] != None:
            walk_tree(nodes)


if __name__ == "__main__":
    # a = [[0]*8 for i in range(10)]
    #
    # print  os.path.realpath(__file__)
    from framework.util import strs

    nodes = strs.path_to_tree(cats())
    # print nodes
    n, l = walk_tree(nodes)
    print json.dumps(n)
    print '----------------'
    print json.dumps(l)


