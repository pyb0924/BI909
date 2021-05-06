# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiCT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 822)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(15, 0, 772, 761))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.imglabel1 = QLabel(self.layoutWidget)
        self.imglabel1.setObjectName(u"imglabel1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imglabel1.sizePolicy().hasHeightForWidth())
        self.imglabel1.setSizePolicy(sizePolicy1)
        self.imglabel1.setMinimumSize(QSize(320, 320))
        self.imglabel1.setMaximumSize(QSize(320, 320))
        self.imglabel1.setMargin(10)

        self.gridLayout.addWidget(self.imglabel1, 1, 0, 1, 1)

        self.imglabel2 = QLabel(self.layoutWidget)
        self.imglabel2.setObjectName(u"imglabel2")
        sizePolicy1.setHeightForWidth(self.imglabel2.sizePolicy().hasHeightForWidth())
        self.imglabel2.setSizePolicy(sizePolicy1)
        self.imglabel2.setMinimumSize(QSize(320, 320))
        self.imglabel2.setMaximumSize(QSize(320, 320))
        self.imglabel2.setMargin(10)

        self.gridLayout.addWidget(self.imglabel2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.imglabel3 = QLabel(self.layoutWidget)
        self.imglabel3.setObjectName(u"imglabel3")
        sizePolicy1.setHeightForWidth(self.imglabel3.sizePolicy().hasHeightForWidth())
        self.imglabel3.setSizePolicy(sizePolicy1)
        self.imglabel3.setMinimumSize(QSize(320, 320))
        self.imglabel3.setMaximumSize(QSize(320, 320))

        self.gridLayout.addWidget(self.imglabel3, 3, 0, 1, 1)

        self.imglabel4 = QLabel(self.layoutWidget)
        self.imglabel4.setObjectName(u"imglabel4")
        sizePolicy1.setHeightForWidth(self.imglabel4.sizePolicy().hasHeightForWidth())
        self.imglabel4.setSizePolicy(sizePolicy1)
        self.imglabel4.setMinimumSize(QSize(320, 320))
        self.imglabel4.setMaximumSize(QSize(320, 320))
        self.imglabel4.setBaseSize(QSize(0, 0))
        self.imglabel4.setMargin(10)

        self.gridLayout.addWidget(self.imglabel4, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.openButton = QPushButton(self.layoutWidget)
        self.openButton.setObjectName(u"openButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei")
        font1.setPointSize(12)
        self.openButton.setFont(font1)

        self.verticalLayout.addWidget(self.openButton)

        self.parallelButton = QPushButton(self.layoutWidget)
        self.parallelButton.setObjectName(u"parallelButton")
        sizePolicy2.setHeightForWidth(self.parallelButton.sizePolicy().hasHeightForWidth())
        self.parallelButton.setSizePolicy(sizePolicy2)
        self.parallelButton.setFont(font1)

        self.verticalLayout.addWidget(self.parallelButton)

        self.reconstructButton = QPushButton(self.layoutWidget)
        self.reconstructButton.setObjectName(u"reconstructButton")
        sizePolicy2.setHeightForWidth(self.reconstructButton.sizePolicy().hasHeightForWidth())
        self.reconstructButton.setSizePolicy(sizePolicy2)
        self.reconstructButton.setFont(font1)

        self.verticalLayout.addWidget(self.reconstructButton)

        self.filterReconstructionButton = QPushButton(self.layoutWidget)
        self.filterReconstructionButton.setObjectName(u"filterReconstructionButton")
        sizePolicy2.setHeightForWidth(self.filterReconstructionButton.sizePolicy().hasHeightForWidth())
        self.filterReconstructionButton.setSizePolicy(sizePolicy2)
        self.filterReconstructionButton.setFont(font1)

        self.verticalLayout.addWidget(self.filterReconstructionButton)

        self.closeButton = QPushButton(self.layoutWidget)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy2.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy2)
        self.closeButton.setFont(font1)

        self.verticalLayout.addWidget(self.closeButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u539f\u56fe\u50cf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6295\u5f71\u6b63\u5f26\u56fe", None))
        self.imglabel1.setText("")
        self.imglabel2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u63a5\u53cd\u6295\u5f71\u91cd\u5efa\u56fe\u50cf", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u53cd\u6295\u5f71\u91cd\u5efa\u56fe\u50cf", None))
        self.imglabel3.setText("")
        self.imglabel4.setText("")
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.parallelButton.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u884c\u675f\u626b\u63cf", None))
        self.reconstructButton.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u63a5\u53cd\u6295\u5f71", None))
        self.filterReconstructionButton.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u53cd\u6295\u5f71", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
    # retranslateUi

