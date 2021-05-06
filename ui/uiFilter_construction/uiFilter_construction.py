# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiFilter_construction.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_filterWindow(object):
    def setupUi(self, filterWindow):
        if not filterWindow.objectName():
            filterWindow.setObjectName(u"filterWindow")
        filterWindow.resize(414, 249)
        self.affirmButton = QPushButton(filterWindow)
        self.affirmButton.setObjectName(u"affirmButton")
        self.affirmButton.setGeometry(QRect(160, 210, 75, 29))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.affirmButton.sizePolicy().hasHeightForWidth())
        self.affirmButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.affirmButton.setFont(font)
        self.layoutWidget = QWidget(filterWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(19, 21, 381, 171))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.filterNameBox = QComboBox(self.layoutWidget)
        self.filterNameBox.addItem("")
        self.filterNameBox.addItem("")
        self.filterNameBox.addItem("")
        self.filterNameBox.addItem("")
        self.filterNameBox.addItem("")
        self.filterNameBox.addItem("")
        self.filterNameBox.setObjectName(u"filterNameBox")
        font1 = QFont()
        font1.setPointSize(16)
        self.filterNameBox.setFont(font1)

        self.gridLayout.addWidget(self.filterNameBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.thetaNumEdit = QLineEdit(self.layoutWidget)
        self.thetaNumEdit.setObjectName(u"thetaNumEdit")
        self.thetaNumEdit.setFont(font1)
        self.thetaNumEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.thetaNumEdit, 0, 1, 1, 1)


        self.retranslateUi(filterWindow)

        QMetaObject.connectSlotsByName(filterWindow)
    # setupUi

    def retranslateUi(self, filterWindow):
        filterWindow.setWindowTitle(QCoreApplication.translate("filterWindow", u"Form", None))
        self.affirmButton.setText(QCoreApplication.translate("filterWindow", u"\u786e\u5b9a", None))
        self.filterNameBox.setItemText(0, QCoreApplication.translate("filterWindow", u"None", None))
        self.filterNameBox.setItemText(1, QCoreApplication.translate("filterWindow", u"hamming", None))
        self.filterNameBox.setItemText(2, QCoreApplication.translate("filterWindow", u"shepp-logan", None))
        self.filterNameBox.setItemText(3, QCoreApplication.translate("filterWindow", u"cosine", None))
        self.filterNameBox.setItemText(4, QCoreApplication.translate("filterWindow", u"ramp", None))
        self.filterNameBox.setItemText(5, QCoreApplication.translate("filterWindow", u"hann", None))

        self.filterNameBox.setCurrentText(QCoreApplication.translate("filterWindow", u"None", None))
        self.label_2.setText(QCoreApplication.translate("filterWindow", u"theta num", None))
        self.label.setText(QCoreApplication.translate("filterWindow", u"filter name", None))
        self.thetaNumEdit.setText(QCoreApplication.translate("filterWindow", u"180", None))
        self.thetaNumEdit.setPlaceholderText("")
    # retranslateUi

