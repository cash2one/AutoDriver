# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import datetime, string, re
import uuid


def to_datetime(str_time):
    return datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')


def isFloat(str_number):
    pattern = re.compile(r'^\d+\.?\d+$|^\d+$')
    match = pattern.match(str_number)
    if match:
        return True
    else:
        return False


def isNumber(str_number):
    pattern = re.compile(r'^[(-?\d+\.\d+)|(-?\d+)|(-?\.\d+)]+$')
    match = pattern.match(str_number)
    if match:
        return True
    else:
        return False


def longToInt(value):
    if value > 2147483647:
        return (value & (2 ** 31 - 1))
    else:
        return value


def to_long(str_number):
    if not isNumber(str_number):
        return None

    if isFloat(str_number):
        return long(string.atof(str_number))
    else:
        return string.atol(str_number)


def combine_url(host, api='', params=None):
    '''
    接口地址拼接
    :param host:
    :param api:
    :param params:
    :return:
    '''
    param_str = ''
    if params != None:
        for p in params:
            new_param = p + '=' + params[p]
            if len(param_str.strip()) == 0:
                param_str += '?' + new_param
            else:
                param_str += '&' + new_param

    uri = ''
    if host[-1] == '/':
        # 服务器地址是否末尾带斜杠/
        if api.find('/') == 0:
            uri = host + api[1:len(api)] + param_str
        else:
            uri = host + api + param_str
    else:
        if api.find('/') == 0:
            uri = host + api + param_str
        else:
            uri = host + '/' + api + param_str
    return uri


def to_int(str_number):
    if not isNumber(str_number):
        return None

    if isFloat(str_number):
        return int(string.atof(str_number))
    else:
        return longToInt(str_number)


def path_to_tree(cat_list):
    '''
    路径转化为树
    :param cat_list:
    :return:
    '''
    nodes = []
    for ca in cat_list:
        t = tuple(ca.split('\\'))

        for i in range(0, len(t)):
            node = {}
            index = len(t) - 1
            current = t[index - i]

            #node[current]=[]
            node['name'] = current
            self_name = (ca.split(current)[0] + current).replace('\\', '')
            node['self_id'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, self_name.encode('utf-8')))
            if index - i - 1 < 0:
                node['parent_id'] = None
            else:
                parent_name = ca.split(current)[0].replace('\\', '')
                node['parent_id'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, parent_name.encode('utf-8')))
            if not node in nodes:
                nodes.append(node)

    return nodes




