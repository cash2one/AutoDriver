#!/usr/bin/env python
#coding=gb2312


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt4 import QtCore


class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return 1#len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0


class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, data, parent=None):
        super(TreeModel, self).__init__(parent)

        self.rootItem = TreeItem((u'��Ŀ'))

        #self.setupModelData(data.split('\n'), self.rootItem)
        self.setupModelData(data, self.rootItem)
        self.checkLisk = []

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None
        
        item = index.internalPointer()
        
        if role == QtCore.Qt.CheckStateRole:          #��ѡ������checkbox
            if item.parent() == self.rootItem:        #����Ǹ��Ļ���ֱ�ӷ���
                return None
            if item.childCount()>0:                   #�����������Ļ���ֱ�ӷ��أ�������Ը�����Ҫ����������Ҫ����ѡ���ʱ�򣬱��뱣��
                return None
            if index.column()==0:
                for x in self.checkLisk:              #�������Ƿ���checkList�У�����ڽ�����Ϊѡ��״̬
                    if x == index:
                        return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked

        if role != QtCore.Qt.DisplayRole:
            return None

        return item.data(index.column())

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.CheckStateRole and index.column()==0:  
            if value == QtCore.Qt.Unchecked:
                self.checkLisk.remove(index)
                self.emit(QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
                          index, index)    
            else:
                self.checkLisk.append(index)
                self.emit(QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
                          index, index)
            return True

    def flags(self, index):        
        if not index.isValid() :
            return QtCore.Qt.NoItemFlags        
        result = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable        
        if index.column()==0:                          #ֻ�õ�һ����ʾcheckbox
            result |= QtCore.Qt.ItemIsUserCheckable            
        return result


    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()


    def setupModelData1(self, lines, parent):
        pass

    def setupModelData(self, lines, parent):
        parents = [parent]
        indentations = [0]

            # lineData:
                # Read the column data from the rest of the line.
            #columnData = lineData['api']#[s for s in lineData.split('\t') if s]
        for line in lines:
            columnData=()
            position=0
            for api in line['api']:
                position=len(api)
                columnData+=(api['displayName'],)

            #parents.append(parents[-1].child(parents[-1].childCount() - 1))

            if position > indentations[-1]:
                # The last child of the current parent is now the new
                # parent unless the current parent has no children.

                if parents[-1].childCount() > 0:
                    parents.append(parents[-1].child(parents[-1].childCount() - 1))
                    indentations.append(position)

            else:
                while position < indentations[-1] and len(parents) > 0:
                    parents.pop()
                    indentations.pop()

            # Append a new item to the current parent's list of children.
            parents[-1].appendChild(TreeItem(columnData, parents[-1]))



# if __name__ == '__main__':
#
#     import sys
#
#     app = QtGui.QApplication(sys.argv)
#
#     f = QtCore.QFile(':/default.txt')
#     f.open(QtCore.QIODevice.ReadOnly)
#     model = TreeModel(f.readAll())
#     f.close()
#
#     view = QtGui.QTreeView()
#     view.setModel(model)
#     view.setWindowTitle("Simple Tree Model")
#     view.show()
#     sys.exit(app.exec_())