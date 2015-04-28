__author__ = 'ggh'


def over_all_case(ui):
    try:
        from PyQt4 import QtCore

        ui.emit(QtCore.SIGNAL("over_all_case"))
    except ImportError:
        pass


def finish_case(ui, data):
    try:
        from PyQt4 import QtCore

        if ui != None:
            ui.emit(QtCore.SIGNAL("finish_case"), data)
    except ImportError:
        pass
