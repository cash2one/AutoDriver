__author__ = 'xiuhong'

import templates


def result(data,link_names):
    trs = ''
    li_str = ''
    pass_count = 0
    fail_count = 0
    error_count = 0

    for r in data:

        td = ''
        td_status = ''
        for i in range(0,len(r)):
            if type(r[i]) is unicode:
                td += '<td>%s</td>\n' % str(r[i].encode('utf-8'))
            else:
                td += '<td>%s</td>\n' % str(r[i])
        tr = '<tr class="%s">\n%s</tr>\n' % (td_status,td)
        trs += tr

    data_list = templates.HTML_TABLE_RESULTS % dict(tbody = trs)

    link_names_sort = sorted(link_names)
    for n in range(0,len(link_names_sort)):
        li_str += '<li><a href="%s.html">%s</a></li>' % (link_names_sort[n],n+1)

    result_str = 'pass:%s, fail:%s, error:%s' %(pass_count,fail_count,error_count)

    html_dict = dict(
        report_time = '2014',
        result_num = result_str,
        li = li_str,
        PassCount = 0,
        FailureCount = 0,
        ErrorCount = 0,
        result_data = data_list,
    )

    html = templates.HTML_HEADER
    return html % html_dict

def detail(data):
    pass
