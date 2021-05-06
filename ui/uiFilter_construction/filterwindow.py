from ui.uiFilter_construction.uiFilter_construction import Ui_filterWindow
from PySide2 import QtWidgets
from PySide2.QtCore import Signal


class FilterWindow(QtWidgets.QMainWindow, Ui_filterWindow):
    signal = Signal(str, int)

    def __init__(self):
        super(FilterWindow, self).__init__()
        self.setupUi(self)
        self.errorBox = QtWidgets.QMessageBox()
        self.affirmButton.clicked.connect(self.affirm)

    def affirm(self):
        filterName = self.filterNameBox.currentText()
        angleNum = self.thetaNumEdit.text()
        if filterName == 'None':
            filterName = None

        try:
            angleNum = int(angleNum)
        except ValueError:
            self.errorBox.critical(self, 'Error', '输入错误！请输入一个数字')
        else:
            if angleNum < 0:
                self.errorBox.critical(self, 'Error', '输入错误！请输入一个非负整数')
            else:
                self.close()
                self.signal.emit(filterName, angleNum)
