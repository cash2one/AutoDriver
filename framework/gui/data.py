# coding=utf-8
__author__ = 'ggh'

import os
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def walk_testcase(test_case_path):
    for parent, dirnames, filenames in os.walk(test_case_path):
        return dirnames
        # if len(dirnames) == 0:
        #     #dir_name = parent[len(data_path) + 1:len(parent)]
        #     files = fs.filter_files(parent, 'test', 'py')
        #     #return files


def get_task_data(data_path):
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
            db = dir_name.replace(os.sep, '_') + '.db'  # str(uuid.uuid1()).replace('-', '') + '.db'
            task_list += (
                {'row': (
                    '00' + str(t_no), dir_name, u'自动化', u'未开始', u'普通', 'jira.displayName', 'box.jira.displayName',
                    '2014-07-02 17:35:00', '2014-07-02 17:35:00', '', '2014-07-02 17:35:00', 'desc'),
                 'task': tasks, 'result': db},
            )
    return task_list

    #task_data = temp_task_data(PATH('../testcase'))