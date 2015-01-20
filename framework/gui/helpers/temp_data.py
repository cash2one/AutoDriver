# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import uuid
from framework.util import fs
from framework.core import the

displayName = the.jira.displayName
print displayName


def task_list(data_path):
    task_list = ()
    t_no = 0
    for parent, dirnames, filenames in os.walk(data_path):
        if len(dirnames) == 0:
            dir_name = parent[len(data_path) + 1:len(parent)]
            files = fs.filter_files(parent, 'test', 'py')

            scripts = []
            for c in files:
                sc = {}
                sc['name'] = c
                sc['source'] = dir_name
                sc['loop'] = 1  # 写入自动化脚本 和执行次数到case_dict
                sc['desc'] = ''
                scripts.append(sc)

            tasks = []
            if len(scripts) > 0:
                task = {}
                task['cases'] = scripts
                task['status'] = 0
                task['path'] = parent
                tasks.append(task)

            t_no += 1
            db = str(uuid.uuid1()).replace('-', '') + '.db'
            task_list += (
                {'row': (
                    '00' + str(t_no), dir_name, u'自动化', u'未开始', u'普通', displayName, displayName,
                    '2014-07-02 17:35:00', '2014-07-02 17:35:00', '', '2014-07-02 17:35:00', 'desc'),
                 'task': tasks, 'result': db},
            )
    return task_list