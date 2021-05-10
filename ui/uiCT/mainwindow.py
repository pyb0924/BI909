from ui.uiCT.uiCT import Ui_MainWindow
from ui.uiFilter_construction.filterwindow import FilterWindow
from PySide2 import QtWidgets
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QImage, QPixmap
import cv2
import numpy as np
from src.radon import radon
from src.iradon import iradon
from time import time


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.filedialog = QtWidgets.QFileDialog()
        self.errorBox = QtWidgets.QMessageBox()
        self.filterWindow = FilterWindow()
        self.workThread = WorkThread()

        self.image = None
        self.projectionImage = None
        self.reconstructImage = None

        self.openButton.clicked.connect(self.open_img)
        self.parallelButton.clicked.connect(self.bgParallelScan)
        self.reconstructButton.clicked.connect(self.reconstruct)
        self.filterReconstructionButton.clicked.connect(self.openFilterWindow)
        self.filterWindow.signal.connect(self.doReconstruct)
        self.closeButton.clicked.connect(self.close)
        self.workThread.signal.connect(self.returnWork)

    def open_img(self):
        self.statusbar.showMessage('正在打开文件……')
        filepath, filetype = self.filedialog.getOpenFileName(
            self, '选择要处理的图片',
            r'./', '图片类型(*.jpg *.jpeg *.png *.bmp)'
        )
        if filepath:
            self.image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            self.show_img(self.image, self.imglabel1)
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

    def show_img(self, image, label):
        image = (image / np.max(image) * 256).astype('uint8')
        qImage = QImage(image, image.shape[1], image.shape[0], np.min(image.shape),
                        QImage.Format_Grayscale8)
        qPix = QPixmap(qImage).scaled(label.width(), label.height())
        label.setPixmap(qPix)

    def set_all_button(self, flag):
        button_list = ['open', 'parallel', 'reconstruct', 'filterReconstruction', 'close']
        for button_name in button_list:
            button = getattr(self, button_name + 'Button')
            button.setEnabled(flag)

    def bgParallelScan(self):
        if self.image is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        self.set_all_button(False)
        self.statusbar.showMessage('正在进行: 平行束扫描')
        self.set_all_button(False)
        self.workThread.set_params(radon, self.image)
        self.workThread.start()

    def reconstruct(self):
        if self.image is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        if self.projectionImage is None:
            self.errorBox.critical(self, 'Error','请先进行平行束扫描')

        self.statusbar.showMessage('正在进行: 直接反投影重建')
        self.set_all_button(False)
        self.workThread.set_params(iradon, self.projectionImage, 180)
        self.workThread.start()

    def openFilterWindow(self):
        if self.image is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        if self.projectionImage is None:
            self.errorBox.critical('请先进行平行束扫描')
        self.filterWindow.show()

    def doReconstruct(self, filter_name, angleNum):
        self.statusbar.showMessage('正在进行: 滤波反投影重建')
        self.set_all_button(False)
        self.workThread.set_params(iradon, self.projectionImage, angleNum, filter_name)
        self.workThread.start()

    def returnWork(self, result_img, workType, workTime):
        work_dict = {
            1: '平行束扫描', 2: '直接反投影重建', 3: '滤波反投影重建'
        }
        if workType == 1:
            self.projectionImage = result_img
            self.show_img(self.projectionImage, self.imglabel2)
        elif workType == 2:
            self.reconstructImage = result_img
            self.show_img(self.reconstructImage, self.imglabel3)
        elif workType == 3:
            self.reconstructImage = result_img
            self.show_img(self.reconstructImage, self.imglabel4)

        self.set_all_button(True)
        self.statusbar.showMessage('已完成:{0}，用时t={1:.2f}s'.format(work_dict[workType], workTime))


class WorkThread(QThread):
    signal = Signal(np.ndarray, int, float)  # 1:scan 2:direct 3:filter

    def __init__(self) -> None:
        super().__init__()
        self.method = None
        self.params = None

    def set_params(self, method, *params):
        self.method = method
        self.params = params

    def run(self) -> None:
        start = time()
        result = self.method(*self.params)
        end = time()
        self.signal.emit(result, len(self.params), end - start)
