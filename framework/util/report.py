# coding=utf-8
__author__ = 'Administrator'

import os,re
import xlwt
import my_sqlite
import consts

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

db_path = PATH('../db/')
report_path = PATH('../report/')


def find_last_db():
    dbs=[]
    lists = os.listdir(db_path)

    for a in lists:
        f = os.path.basename(a)
        pattern = re.compile(r'^[0-9]*$')
        match = pattern.match(os.path.splitext(f)[0])

        if '.db' in os.path.splitext(f)[1] and match:
            dbs.append(match.group())

    if len(dbs)>0:
        db_file_name = str(max(dbs))

        path = os.path.join(db_path,'%s.db' % db_file_name)
        dbm = my_sqlite.DBManager(path)
        return dbm.fetchall('select * from info'),db_file_name
    else:
        return None

def write_html():
    datas,file_name = find_last_db()
    if find_last_db()==None:
        return

    trs=''
    for data in datas:
        tds = ''
        for d in data:
            tds += '<td>\n%s</td>\n' % str(d)
        trs+='<tr>'+tds+'</tr>\n'

    html = consts.HTML % dict(tbody = trs)

    path = os.path.join(report_path,'%s.html' % file_name)
    fi = open(path,'w')
    fi.write(html)
    fi.close()

    return file_name+'.html'


def write_xls(task_type):
    datas,file_name = find_last_db()
    if find_last_db()==None:
        return

    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet('sheet', cell_overwrite_ok=True)
    title=[]

    if task_type==consts.TASK_SERVER:
        title = ['id','CPU(%)','Memory(MB)','Net1_sent','Net1_recv','Net2_sent','Net2_recv','UpdateTime']
    elif task_type==consts.TASK_LOCAL:
        title = ['id','resp_time','status_code','update_time']

    t_index = 0
    for t in title:
        sheet.write(0,t_index,t)
        t_index+=1

    row_num = 1
    for row_index in range(0,len(datas)):
        for col_index in range(0,len(datas[row_index])):
            #sheet.setColWidth(col,3020)
            if col_index == 0:
                sheet.col(col_index).width = 1200
            elif col_index == 1:
                sheet.col(col_index).width = 2200
            else:
                sheet.col(col_index).width = 6200
            sheet.write(row_num, col_index, datas[row_index][col_index])
        row_num += 1

    try:
        path = os.path.join(report_path,'%s.xls' % file_name)
        wbk.save(path)
    except IOError:
        print u'excel is open.'

    return file_name+'.xls'

