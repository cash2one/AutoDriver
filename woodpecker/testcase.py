# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from framework.util import fs

from woodpecker.views import testcase_ui

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

data = [
    ("Alice", [
        ("Keys", []),
        ("Purse", [
            ("Cellphone", [])
        ])
    ]),
    ("Bob", [
        ("Wallet", [
            ("Credit card", []),
            ("Money", [])
        ])
    ])
]

demo = {
    "订单管理": [
        {"待处理订单": [{"查询失败": []}]},
        {
            "历史订单": [
                {"查询成功": [{"查询成功1": []}]},
                {"查询f成功": []}
            ]
        }
    ],
    "客户管理": [
        {
            "客户投诉": [
                {"审核": [{"结果": []}]},
                {"回访": []}
            ]
        }
    ]
}


class TestCaseForm(QWidget, testcase_ui.Ui_Form):
    def __init__(self):
        super(TestCaseForm, self).__init__()

        self.setupUi(self)

        cat = [u'订单管理\历史订单\查询成功\查询成功1', u'订单管理\历史订单\查询f成功', u'客户管理\客户投诉\回访', u'客户管理\客户投诉\审核', u'订单管理\待处理订单\查询失败',
               u'客户管理\客户投诉\审核\结果']

        nodes = fs.path_to_dict(cat)
        print nodes
        datas = fs.walk_tree(nodes)

        self.model = QStandardItemModel()
        self.addItems(self.model, datas)
        self.treeView.setModel(self.model)

        title = 'fff'.encode('utf-8')
        self.model.setHorizontalHeaderLabels([self.tr(title)])

    def addItems(self, parent, nodes):
        for node in nodes:
            item = QStandardItem(node)
            parent.appendRow(item)
            nd = nodes[node]
            if len(nodes[node]) > 0:
                print 'fff::::::',nd
                self.addItems(item, nd)

                # for i in range(0, len(nodes)):
                # item = QStandardItem(nodes[i]['name'])
                #     parent.appendRow(item)
                #     for n in range(0, len(nodes)):
                #         if nodes[i]['self_id'] == nodes[n]['parent_id']:
                #             item_sub = QStandardItem(nodes[n]['name'])
                #
                #             # item_sub.appendRow(nodes[n]['name'])
                #             item.appendRow(item_sub)
                #             self.addItems(item, children)
                #
                #
                #             # nodes[i][i_name].append({n_name: nodes[n][n_name]})
                #
                #     if nodes[i]['parent_id'] == None:
                #         self.model.appendRow(item)
