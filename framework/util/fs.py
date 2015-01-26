# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import re
import shutil
import ConfigParser
import uuid
import const
from xml.etree import cElementTree


"""
各种文件操作方法 集合
"""

base_dir = os.path.dirname(os.path.dirname(__file__))

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def task_container(path_str, selections):
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)

    all = {}
    options = conf.options(selections)
    for opt in options:  # 取出sections内的所有options
        str_val = conf.get(selections, opt)
        dictCase = {}
        dictCase[const.TASK_CONFIG] = str_val
        dictCase[const.PRODUCT] = None
        all[opt.lower()] = dictCase
    return all


# def init_project(path_str):
# conf = ConfigParser.ConfigParser()
# conf.read(path_str)
#
# sections = conf.sections()
# section_list = {}
# for sect in sections:
# dictCase = {}
# options = conf.options(sect)
#         for opt in options:  # 取出sections内的所有options
#             str_val = conf.get(sect, opt)
#             dictCase[opt] = str_val.decode('utf-8')
#
#         dictCase[const.PRODUCT] = None
#         section_list[sect] = dictCase
#
#     return section_list


def parser_to_dict(path_str):
    '''
    selections组成一个dict
    :param path_str:
    :return:
    '''
    ands = {}
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    sec = conf.sections()
    for s in sec:
        ands[s] = None
    return ands


def parserConfig(path_str):
    '''
    读取配置文件内所有selection
    :param path_str:
    :return:
    '''
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)

    sections = conf.sections()
    section_list = {}
    for sect in sections:
        dictCase = {}
        options = conf.options(sect)
        for opt in options:  # 取出sections内的所有options
            str_val = conf.get(sect, opt)
            dictCase[opt] = str_val.decode('utf-8')

        section_list[sect] = dictCase

    return section_list


def readConfigs(path_str, selections):
    '''
    读取指定selection的配置文件
    :param path_str:
    :param selections:
    :return:
    '''
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)

    dictCase = {}
    options = conf.options(selections)
    for opt in options:  # 取出sections内的所有options
        str_val = conf.get(selections, opt)
        dictCase[opt] = str_val.decode('utf-8')

    return dictCase


def readConfig(path_str, selections, opt):
    '''
    读取单个selections的option
    :param path_str:
    :param selections:
    :param opt:
    :return:
    '''
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    return conf.get(selections, opt)


# 写入task配置文件
def writeConfig(path_str, selections, opt, val):
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    conf.set(selections, opt, val)
    f = open(path_str, 'w')
    conf.write(f)
    f.close()


def read_xml(xml_path):
    per = cElementTree.parse(xml_path)
    p = per.findall('interface')
    infs = []
    for x in p:
        inf = x.attrib
        inf['parameter'] = []
        for c in x.getchildren():
            inf['parameter'].append(c.attrib)
        infs.append(inf)

    return infs


def newFile(origin_file, new_file, xs):
    '''
    读取文件，并替换其中的值，生成一个新的文件存放到指定目录。
    :param origin_file:
    :param new_file:
    :param xs:
    :return:
    '''
    if not os.path.exists(origin_file):
        return

    try:
        #remove old temp
        os.remove(new_file)
    except os.error:
        pass

    fi = open(origin_file)
    fo = open(new_file, 'w')

    for line in fi.readlines():
        if not line:
            break

        elif '{{description}}' in line:
            fo.write(line.replace('{{description}}', xs['desc'].encode('utf-8')))
        elif '{{expectation}}' in line:
            fo.write(line.replace('{{expectation}}', xs['exp'].encode('utf-8')))
        else:
            fo.write(line)
            # 多参数替换时考虑的代码
            # for i in range(0,len(origin_args)):
            #     if origin_args[i] in line:
            #         fo.write(line.replace(origin_args[i], xs_value[i].encode('utf-8')))

    fi.close()
    fo.close()


def newFileFromTemplates(new_file, xs):
    '''
    读取模板，并插入参数，生成新的文件到指定目录
    :param new_file:
    :param xs:
    :return:
    '''
    try:
        #remove old temp
        os.remove(new_file)
    except os.error:
        pass

    fo = open(new_file, 'w')

    dict_val = dict(
        no=xs['no'],
        desc=xs['desc'].encode('utf-8'),
        exp=xs['exp'].encode('utf-8'),
    )

    if const.FLOW_NAME in xs['cat']:
        flow_str = const.INTERFACE_FLOW % dict_val
    else:
        flow_str = const.INTERFACE_NON_FLOW % dict_val

    fo.write(const.INTERFACE_HEADER + flow_str)

    fo.close()


def prepareFile(data, src, tar):
    '''
    文件复制及替换内容
    :param data:
    :return:
    '''
    for xs in data:
        if xs['script'] == '':
            script = xs['no']
        else:
            script = xs['script']

        if const.FLOW_NAME in xs['cat']:
            cat = xs['cat'].replace('_' + const.FLOW_NAME, '')
        else:
            cat = xs['cat']

        src_sub = '%s/%s.py' % (cat.replace('_', '/'), script)
        src_str = os.path.join(src, src_sub)  #src+'%s/%s.py' % (cat.replace('_','/'),script)

        tar_sub = 'test_%s_%s.py' % (cat, script)
        case_str = os.path.join(tar, tar_sub)


        # 文件名太长，准备用uuid替代
        # name = cat_val+script_val
        # guid = uuid.uuid3(uuid.NAMESPACE_DNS,name.encode('utf-8'))
        # case_str = case_dir+'test_'+str(guid).replace('-','')+'.py'
        #template_str = src_dir + temp

        #接口的参数都是读取自xls,文件需要替换参数

        if const.INTERFACE_FOLDER in cat:
            if xs['script'] == '':  #script为空，则自动读取预置文件
                newFileFromTemplates(case_str, xs)
            else:
                #接口的文件夹不管xls后缀如何变，都用autobook_interface
                new_src_str = src_str.replace('\\', '/')
                pattern = re.compile(r'(?<=interface/)([^/].*/)?(?=[^.]*.py)')
                match = pattern.search(new_src_str)
                if match:
                    #正则没取准确，先用/分割下
                    mg = match.group().split('/')
                    new_src = new_src_str.replace(mg[-2] + '/', '')

                    newFile(new_src, case_str, xs)
        else:  #覆盖testcase已经存在的文件，所以注释and not os.path.exists(case_file):
            if os.path.exists(src_str):
                shutil.copy(src_str, case_str)


def filter_files(dirs, start_str, end_str):
    test = re.compile("^%s.*?.%s$" % (start_str, end_str), re.IGNORECASE)
    return filter(test.search, os.listdir(dirs))


def path_to_dict(cat_list):
    '''
    路径字符串转化为带父子id的字典
    :param cat_list:
    :return:
    '''
    cats = list(set(cat_list))  # 去重

    nodes = []
    for cat in cats:
        t = tuple(cat.split('\\'))

        for i in range(0, len(t)):
            node = {}
            index = len(t) - 1
            current = t[index - i]

            node['name'] = current
            node[current] = []
            self_name = (cat.split(current)[0] + current).replace('\\', '')
            node['self_id'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, self_name.encode('utf-8')))
            if index - i - 1 < 0:
                node['parent_id'] = None
            else:
                parent_name = cat.split(current)[0].replace('\\', '')
                node['parent_id'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, parent_name.encode('utf-8')))
            if not node in nodes:
                nodes.append(node)

    return nodes


def walk_tree(nodes):
    '''
    读取路径字典的集合
    :param nodes:
    :return:
    '''
    new_list = []
    new_dict = {}
    for i in range(0, len(nodes)):
        i_name = ''
        for n in range(0, len(nodes)):
            if nodes[i]['self_id'] == nodes[n]['parent_id']:
                n_name = nodes[n]['name']
                i_name = nodes[i]['name']
                nodes[i][i_name].append({n_name: nodes[n][n_name]})

        if nodes[i]['parent_id'] == None:
            new_dict = dict(new_dict, **nodes[i])
            #new_list.append(nodes[i])
    del new_dict['name']
    del new_dict['self_id']
    del new_dict['parent_id']
    return new_dict  #new_list


def walk_tree_tuple(nodes):
    '''
    读取路径字典的集合
    :param nodes:
    :return:
    '''
    new_dict = ()
    for i in range(0, len(nodes)):
        i_name = ''
        for n in range(0, len(nodes)):
            if nodes[i]['self_id'] == nodes[n]['parent_id']:
                n_name = nodes[n]['name']
                i_name = nodes[i]['name']
                print nodes[i]
                nodes[i] += ((n_name, nodes[n]['name']),)

        if nodes[i]['parent_id'] == None:
            new_dict += nodes[i]  #dict(new_dict, **nodes[i])

    return new_dict  #new_list


#执行操作系统命令
def os_command(cmd):
    os_name = os.name
    if os_name == "nt":
        print("Windows Command")
    else:
        print("Unix/Linux Command")
    os.system(cmd)