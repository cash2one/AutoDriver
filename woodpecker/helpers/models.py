# coding=utf-8

def sql():
    tables = {}

    News = '''
    Title varchar(100) NOT NULL,
    Category varchar(200) NOT NULL,
    Link varchar(500) NULL,
    UpdateTime datetime NOT NULL
    '''
    tables.setdefault('News', News)


    # return tables
    list = []
    for i in range(0, len(tables)):
        k = tables.keys()[i]
        v = tables.values()[i]
        sql_str = 'create table if not exists %s (id integer primary key,%s)' % (k, v)
        list.append(sql_str)
    return list
