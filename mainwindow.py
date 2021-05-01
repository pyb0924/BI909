from ui.uiCT import Ui_MainWindow
from PySide2 import QtWidgets
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QThread, Signal
import cv2
import numpy as np
from src.radon import radon
from src.iradon import iradon
from time import time


def show_img(image, label):
    image = (image / np.max(image) * 256).astype('uint8')
    try:
        qImage = QImage(image, image.shape[1], image.shape[0], np.min(image.shape),
                        QImage.Format_Grayscale8)
        qPix = QPixmap(qImage).scaled(label.width(), label.height())
        label.setPixmap(qPix)
    except ValueError:
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.filedialog = QtWidgets.QFileDialog()
        self.errorBox = QtWidgets.QMessageBox()

        self.image = None
        self.result = None
        self.projectionImage = None
        self.reconstructImage = None

        self.openButton.clicked.connect(self.open_img)
        self.parallelButton.clicked.connect(self.parallelScan)
        self.reconstructButton.clicked.connect(self.reconstruct)

    def open_img(self):
        self.statusbar.showMessage('正在打开文件……')
        filepath, filetype = self.filedialog.getOpenFileName(
            self, '选择要处理的图片',
            r'./', '图片类型(*.jpg *.jpeg *.png *.bmp)'
        )
        if filepath:
            self.image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            show_img(self.image, self.imglabel1)
            self.statusbar.showMessage('图片打开成功')
        else:
            self.statusbar.showMessage('图片打开失败')

    def save_img(self):
        if self.resultimage is None:
            self.errorBox.critical(self, 'Error', '当前没有已打开的文件！')
            return

        filepath, filetype = self.filedialog.getSaveFileName(
            self, '保存图片', r'./', '图片类型(PNG File(*.png) JPEG File(*.jpg))'
        )
        if filepath:
            cv2.imwrite(filepath, self.resultimage)
            self.statusbar.showMessage('文件保存成功')
        else:
            self.statusbar.showMessage('文件保存失败')

    def parallelScan(self):
        start = time()
        self.projectionImage = radon(self.image)
        end = time()
        self.statusbar.showMessage('已完成: 平行束扫描，用时t={0:.2f}s'.format(end - start))
        show_img(self.projectionImage, self.imglabel2)

    def reconstruct(self):
        start = time()
        self.reconstructImage = iradon(self.projectionImage, filter_name="ramp")
        end = time()
        self.statusbar.showMessage('已完成: 滤波反投影重建，用时t={0:.2f}s'.format(end - start))
        show_img(self.reconstructImage, self.imglabel4)