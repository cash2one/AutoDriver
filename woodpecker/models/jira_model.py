# coding=utf-8

from PyQt4 import QtCore
from framework.util import convert


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        # QtCore.QAbstractTableModel.__init__(self, parent, *args)
        super(MyTableModel, self).__init__(parent, *args)
        self.arraydata = datain
        self.header = (
            u'编号', u'主题', u'经办人', u'报告人', u'优先级', u'状态', u'解决情况', u'创建时间', u'更新时间')

        self.issues_data = []
        for issue in datain:  # dicts['issues']:
            key = issue['key']
            fields = issue['fields']
            summary = fields['summary']
            assignee = fields['assignee']['displayName']
            reporter = fields['reporter']['displayName']
            priority = fields['priority']['name']
            status = fields['status']['name']
            resolution = ''
            if fields['resolution'] != None:
                resolution = fields['resolution']['name']

            created = convert.utc_to_local(fields['created'])
            updated = convert.utc_to_local(fields['updated'])
            iss_tup = (key, summary, assignee, reporter, priority, status, resolution, created, updated)
            self.issues_data.append(iss_tup)


    def rowContent(self, index):
        return self.arraydata[index]

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        # return len(self.arraydata[0])
        # 列内容经过筛选，所以不用arraydata
        return len(self.issues_data[0])

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        # return QtCore.QVariant(self.arraydata[index.row()][index.column()])
        return QtCore.QVariant(self.issues_data[index.row()][index.column()])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.header[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

