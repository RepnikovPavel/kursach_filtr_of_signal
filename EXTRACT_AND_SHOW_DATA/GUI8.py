# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import scipy as sp

from training_block import *
from write_sample2file import *
from load_saples_from_file import *

import pandas as pd

import numpy as np
from matplotlib import cm

from PyQt5 import QtCore, QtGui, QtWidgets

# other lib
import pyqtgraph as pg
# my py files
import load_from_one_file

# for matplotlib embeding
from PyQt5.QtWidgets import QSizePolicy

# ******************************************************************
import matplotlib
import csv

matplotlib.use("Qt5Agg")
# ******************************************************************
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

# for the colormap
# from pylab import pcolor
# import seaborn as sns


# for the debug
# import time
# start_time = time.time()


# for the time controlling
from SUPPORT_FUNC import *

from scipy.ndimage.filters import gaussian_filter


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)

        # self.fig.set(facecolor='k')
        # self.axes = plt.axes(xlim=(0, 11), ylim=(0, 101))
        self.axes = self.fig.add_subplot(111)

        # эти 2 строчки просаживают производителность
        # self.axes.set_yticks([])
        # self.axes.set_xticks([])
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setParent(parent)

    def plot_color_map(self, pd_table):
        self.axes.clear()

        self.im = plt.imshow(pd_table,
                             aspect='auto',
                             norm=mpl.colors.Normalize(0, sp.pi / 20), interpolation="nearest",
                             cmap=cm.jet
                             )
        # print("--- %s seconds ---" % (time.time() - start_time))
        # self.heatmap = sns.heatmap(pd_table, ax=self.axes,cbar=False, cmap='binary',xticklabels=[],yticklabels=[])
        # print("--- %s seconds ---" % (time.time() - start_time))
        self.draw()

    def for_update_im(self, pd_table, time):
        self.axes.set_title(time)
        self.im.set_data(pd_table)
        self.draw()

    def plot_linear_signal(self, x, y):
        self.axes.clear()
        self.line, = plt.plot(x, y)
        self.draw()

    def for_update_linear_signal(self, x, y):
        self.line.set_data(x, y)
        self.draw()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayout = QtWidgets.QFormLayout(self.tab_4)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = pg.PlotWidget(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('#FFFFFF')
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_4.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem19)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem20)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem21)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_4.addWidget(self.lineEdit_10)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem22)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_4.addWidget(self.lineEdit_11)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem23)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 600, 200, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setGeometry(QtCore.QRect(80, 625, 200, 25))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(280, 600, 200, 25))
        self.pushButton_12.setObjectName("pushButton_12")

        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_12.setGeometry(50, 50, 400, 50)
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_13.setGeometry(50, 100, 200, 50)
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_14.setGeometry(50, 0, 200, 50)
        self.lineEdit_14.setObjectName("lineEdit_14")

        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 150, 200, 50))
        self.pushButton_13.setObjectName("pushButton_13")

        # for training tab
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(250, 150, 200, 50))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(50, 200, 200, 50))
        self.pushButton_15.setObjectName("pushButton_15")

        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(450, 200, 200, 50))
        self.lineEdit_15.setObjectName("lineEdit_15")

        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(250, 250, 200, 50))
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(250, 200, 200, 50))
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_17.setGeometry(QtCore.QRect(50, 250, 200, 50))
        self.pushButton_17.setObjectName("pushButton_17")

        self.pushButton_18 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_18.setGeometry(QtCore.QRect(50, 200, 200, 50))
        self.pushButton_18.setObjectName("pushButton_18")

        # operation with data block:

        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(500, 250, 200, 50))
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.pushButton_19 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_19.setGeometry(QtCore.QRect(500, 300, 200, 50))
        self.pushButton_19.setObjectName("pushButton_19")

        self.pushButton_20 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_20.setGeometry(QtCore.QRect(500, 350, 200, 50))
        self.pushButton_20.setObjectName("pushButton_20")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "load_vtd"))
        self.pushButton_2.setText(_translate("MainWindow", "load_dnew"))
        self.lineEdit.setText(_translate("MainWindow", "vtd_path"))
        self.lineEdit_2.setText(_translate("MainWindow", "dnew_path"))
        self.lineEdit_3.setText(_translate("MainWindow", "ot"))
        self.lineEdit_4.setText(_translate("MainWindow", "do"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "data_load"))
        self.pushButton_10.setText(_translate("MainWindow", "plot_line"))
        self.pushButton_3.setText(_translate("MainWindow", "timer1_start"))
        self.pushButton_4.setText(_translate("MainWindow", "timer1_stop"))
        self.lineEdit_5.setText(_translate("MainWindow", "num_ch_for_plot"))
        self.lineEdit_6.setText(_translate("MainWindow", "set time1"))
        self.lineEdit_8.setText(_translate("MainWindow", "velocity1"))
        self.lineEdit_9.setText(_translate("MainWindow", "N1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "one_signal"))
        self.pushButton_9.setText(_translate("MainWindow", "create_color_map"))
        self.pushButton_8.setText(_translate("MainWindow", "plot_color_map"))
        self.pushButton_5.setText(_translate("MainWindow", "timer2_start"))
        self.pushButton_6.setText(_translate("MainWindow", "timer2_stop"))
        self.lineEdit_7.setText(_translate("MainWindow", "set_time2"))
        self.lineEdit_10.setText(_translate("MainWindow", "velocity2"))
        self.lineEdit_11.setText(_translate("MainWindow", "N2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "signal_map"))
        self.pushButton_7.setText(_translate("MainWindow", "data_normalization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  _translate("MainWindow", "operation_with_data_and_marking"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "for_training"))

        self.canvas = MplCanvas(self.graphicsView_2, width=18, height=9)

        self.pushButton_11.setText(_translate("MainWindow", "test_operations"))
        self.pushButton_12.setText(_translate("MainWindow", "plot_spectrum(on_plot_indeces)"))
        self.lineEdit_12.setText(_translate("MainWindow", "00:00:000;00:19:000"))
        self.lineEdit_13.setText(_translate("MainWindow", "type"))
        self.lineEdit_14.setText(_translate("MainWindow", "3;7"))
        self.pushButton_13.setText(_translate("MainWindow", "write_sample_to_file"))
        self.pushButton_18.setText(_translate("MainWindow", "write_example_of_a_fixed_length"))

        # for training tab
        self.pushButton_14.setText(_translate("MainWindow", "load_samples_and_labels"))
        self.pushButton_14.clicked.connect(lambda: self.load_samples_and_labels())

        self.pushButton_15.setText(_translate("MainWindow", "show_signal_and_spectum"))
        self.pushButton_15.clicked.connect(lambda: self.show_signal_and_spectum())

        self.pushButton_16.setText(_translate("MainWindow", "show_sample_number:"))
        self.pushButton_16.clicked.connect(lambda: self.show_sample())

        self.pushButton_17.setText(_translate("MainWindow", "run_training"))
        self.pushButton_17.clicked.connect(lambda: self.run_training())

        self.lineEdit_15.setText(_translate("MainWindow", "3"))
        self.lineEdit_16.setText(_translate("MainWindow", "2;2;4"))

        # data_load block:
        self.pushButton.clicked.connect(lambda: self.load_data_to_data_table_FROM_ONE_FILE())
        self.pushButton_2.clicked.connect(lambda: self.load_data_to_data_table_FROM_ONE_FILE_dnew())
        self.lineEdit.setText(_translate("MainWindow", "D:\\database_for_kursach\\bryansk_2011_04_14\\data\\"))
        self.lineEdit_3.setText(_translate("MainWindow", "250"))
        self.lineEdit_4.setText(_translate("MainWindow", "350"))
        self.lineEdit_2.setText(_translate("MainWindow", "D:\\database_for_kursach\\2013.11.18.Bronnitsy\\leak_5_vn_pop5\\"))

        # one signal block:
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.lineEdit_6.setText(_translate("MainWindow", "00:00:000"))  # timer1
        self.pushButton_10.clicked.connect(lambda: self.create_tmp_line_from_data_table_FROM_ONE_FILE())
        self.pushButton_3.clicked.connect(lambda: self.start_timer1())
        self.pushButton_4.clicked.connect(lambda: self.timer1.stop())

        # lines
        self.tmp_line = []
        self.index_of_plot = 0
        self.start_index1 = 0
        self.index_for_iterations = 0
        self.timer1 = QtCore.QTimer()
        frame = 1000  # в герцах
        self.timer1.setInterval(1000 / frame)
        self.lineEdit_8.setText(_translate("MainWindow", "1"))
        self.lineEdit_9.setText(_translate("MainWindow", "10000"))

        self.N = int(self.lineEdit_9.text())  # число точек на экране
        self.velocity = int(self.lineEdit_8.text())  # во сколько раз быстрее будут проматываться данные из файла

        self.flag_for_connect_1 = True

        # signal map block:
        self.lineEdit_7.setText(_translate("MainWindow", "00:00:000"))  # timer2
        self.pushButton_9.clicked.connect(lambda: self.create_color_map())
        self.pushButton_8.clicked.connect(lambda: self.plot_color_map())
        self.pushButton_5.clicked.connect(lambda: self.start_timer2())
        self.pushButton_6.clicked.connect(lambda: self.timer2.stop())
        # for color_map
        self.pandas_table = []

        self.index_for_iterations2 = 0
        self.start_index2 = 0
        self.timer2 = QtCore.QTimer()
        frame2 = 1000  # в герцах
        self.timer2.setInterval(1000 / frame2)

        self.lineEdit_10.setText(_translate("MainWindow", "100"))
        self.lineEdit_11.setText(_translate("MainWindow", "298206"))

        self.N2 = int(self.lineEdit_11.text())  # число точек на экране
        self.velocity2 = int(self.lineEdit_10.text())  # во сколько раз быстрее будут проматываться данные из файла

        self.flag_for_connect_2 = True

        # operation with data block:
        self.pushButton_7.clicked.connect(lambda: self.data_normilization())
        self.pushButton_11.clicked.connect(lambda: self.test_operations())
        self.pushButton_12.clicked.connect(lambda: self.plot_spectrum())
        self.pushButton_13.clicked.connect(lambda: self.write_sample())
        self.pushButton_18.clicked.connect(lambda: self.write_fixed_sample())

        self.lineEdit_17.setText(_translate("MainWindow", "3"))
        self.pushButton_19.setText(_translate("MainWindow", "load_filter"))
        self.pushButton_19.clicked.connect(lambda: self.load_filtr())

        self.pushButton_20.setText(_translate("MainWindow", "apply_filter"))
        self.pushButton_20.clicked.connect(lambda: self.apply_filter())

        # data
        self.data_table_FROM_ONE_FILE = []

    def load_data_to_data_table_FROM_ONE_FILE_dnew(self):
        file_path = self.lineEdit_2.text()
        ot = int(self.lineEdit_3.text())
        do = int(self.lineEdit_4.text())
        self.data_table_FROM_ONE_FILE = load_from_one_file.load_bronnitsy(file_path, ot, do)
        print(len(self.data_table_FROM_ONE_FILE[0]))
        print(indeces2time(len(self.data_table_FROM_ONE_FILE[0]), RATE=1000))
        print('load done')

        # print(self.data_table_FROM_ONE_FILE[0][:100],sep='\n')

    def start_timer2(self):
        if self.flag_for_connect_2 == True:
            self.timer2.timeout.connect(self.func_for_timer2)
            self.flag_for_connect_2 = False
        self.N2 = int(self.lineEdit_11.text())  # число точек на экране
        self.velocity2 = int(self.lineEdit_10.text())  # во сколько раз быстрее будут проматываться данные из файла
        self.start_index2 = time2indeces(str(self.lineEdit_7.text()), RATE=1000)
        self.timer2.start()

    def func_for_timer2(self):

        l = len(self.data_table_FROM_ONE_FILE[0])

        if (self.start_index2 + self.index_for_iterations2 * self.velocity2 + self.N2 > l):
            self.timer2.stop()
        if (self.start_index2 + self.index_for_iterations2 * self.velocity2 + self.N2 <= l):
            # print("--- %s seconds ---" % (time.time() - start_time))
            buffer = self.pandas_table.loc[:,
                     self.start_index2 + self.index_for_iterations2 * self.velocity2: self.start_index2 + self.index_for_iterations2 * self.velocity2 + self.N2]
            # print("--- %s seconds ---" % (time.time() - start_time))
            str_of_time = indeces2time(index=self.start_index2 + self.index_for_iterations2 * self.velocity2,
                                       RATE=1000)
            self.canvas.for_update_im(buffer, str_of_time)
            self.index_for_iterations2 += 1

    def plot_color_map(self):
        self.N2 = int(self.lineEdit_11.text())
        self.pandas_table = pd.DataFrame(self.data_table_FROM_ONE_FILE)

        self.start_index2 = time2indeces(str(self.lineEdit_7.text()), RATE=1000)
        self.canvas.plot_color_map(self.pandas_table.loc[:,
                                   self.start_index2 + self.index_for_iterations2 * self.velocity2: self.start_index2 + self.index_for_iterations2 * self.velocity2 + self.N2])
        # self.canvas.plot()

    def load_data_to_data_table_FROM_ONE_FILE(self):

        file_path = self.lineEdit.text()
        ot = int(self.lineEdit_3.text())
        do = int(self.lineEdit_4.text())
        self.data_table_FROM_ONE_FILE = load_from_one_file.load_briansk(file_path, ot, do)
        print(indeces2time(len(self.data_table_FROM_ONE_FILE[0]), RATE=1000))
        print('load done')

    def data_normilization(self):
        for i in range(len(self.data_table_FROM_ONE_FILE)):
            tmp_norma = np.linalg.norm(self.data_table_FROM_ONE_FILE[i])
            self.data_table_FROM_ONE_FILE[i] = self.data_table_FROM_ONE_FILE[i] / tmp_norma
            # print(np.max(self.data_table_FROM_ONE_FILE[i]))
        print('normalization done')
        # print(self.data_table_FROM_ONE_FILE[:][:10])

    def create_tmp_line_from_data_table_FROM_ONE_FILE(self):
        # обновление данных для нового файлика
        self.graphicsView.clear()
        self.index_for_iterations = 0

        self.index_of_plot = int(self.lineEdit_5.text())

        Pen = pg.mkPen(color='#00EE00', width=1, style=QtCore.Qt.SolidLine)

        self.start_index1 = time2indeces(str(self.lineEdit_6.text()), RATE=1000)

        x = range(self.N)

        y = self.data_table_FROM_ONE_FILE[self.index_of_plot][
            self.start_index1 + self.index_for_iterations * self.velocity: self.start_index1 + self.index_for_iterations * self.velocity + self.N]
        self.tmp_line = self.graphicsView.plot(x, y, pen=Pen)

    def start_timer1(self):
        if self.flag_for_connect_1 == True:
            self.timer1.timeout.connect(self.func_for_timer1)
            self.flag_for_connect_1 = False
        self.index_for_iterations = 0
        self.N = int(self.lineEdit_9.text())  # число точек на экране
        self.velocity = int(self.lineEdit_8.text())  # во сколько раз быстрее будут проматываться данные из файла
        self.start_index1 = time2indeces(str(self.lineEdit_6.text()), RATE=1000)
        # print(self.start_index1)
        self.timer1.start()

    def func_for_timer1(self):
        l = len(self.data_table_FROM_ONE_FILE[self.index_of_plot])
        if (self.start_index1 + self.index_for_iterations * self.velocity + self.N > l):
            self.timer1.stop()
        if (self.start_index1 + self.index_for_iterations * self.velocity + self.N <= l):
            buffer_y = self.data_table_FROM_ONE_FILE[self.index_of_plot][
                       self.start_index1 + self.index_for_iterations * self.velocity:self.start_index1 + self.index_for_iterations * self.velocity + self.N]
            # buffer_x=range(self.index_for_iterations*self.velocity, self.index_for_iterations*self.velocity + self.N, 1)
            buffer_x = range(self.N)

            str_of_time = indeces2time(index=self.start_index1 + self.index_for_iterations * self.velocity,
                                       RATE=1000)
            self.lineEdit_6.setText(str_of_time)
            self.tmp_line.setData(buffer_x, buffer_y)
            self.index_for_iterations += 1

    def create_color_map(self):

        self.pandas_table = pd.DataFrame(self.data_table_FROM_ONE_FILE)
        # print(self.pandas_table.head())
        print('color map created')

    def test_operations(self):
        median = np.median(self.data_table_FROM_ONE_FILE[self.index_of_plot])
        mean = np.mean(self.data_table_FROM_ONE_FILE[self.index_of_plot])
        print(median, mean, sep='\n')

    def plot_spectrum(self):
        fixed_length = 3 * 1000
        y = get_spectrum(self.data_table_FROM_ONE_FILE[self.index_of_plot][self.start_index1 + self.index_for_iterations:self.start_index1 +self.index_for_iterations+fixed_length])
        x = get_frequencies(self.data_table_FROM_ONE_FILE[self.index_of_plot][self.start_index1 +self.index_for_iterations:self.start_index1 +self.index_for_iterations+fixed_length], 1000)
        self.canvas.plot_linear_signal(x, y)

    def write_sample(self):
        # D:\samples_for_kursach\data
        # D:\samples_for_kursach\metki

        line_of_indeces = self.lineEdit_14.text()
        line_of_times = self.lineEdit_12.text()
        line_of_type = self.lineEdit_13.text()
        line_of_time1, line_of_time2 = line_of_times.split(";")

        index_from_time1 = time2indeces(line_of_time1, 1000)
        index_from_time2 = time2indeces(line_of_time2, 1000)
        type_of_target = line_of_type

        if len(line_of_indeces) == 1:
            index_of_signal = int(line_of_indeces)  # индекс дорожки в загруженных дорожках
            target_data = self.data_table_FROM_ONE_FILE[index_of_signal][index_from_time1:index_from_time2]

            fl_metki = "D:\\samples_for_kursach\\metki"
            fl_data = "D:\\samples_for_kursach\\data"

            write_data_to_folder_and_metka_to_text(fl_data, fl_metki, target_data, type_of_target)
        else:

            index1, index2 = line_of_indeces.split(";")  # будет записано от  включительно  - до включительно
            index1 = int(index1)
            index2 = int(index2)
            index2 += 1
            tmp_target_data = self.data_table_FROM_ONE_FILE[index1:index2]
            target_data = []
            for i in range(len(tmp_target_data)):
                target_data.append([])
                target_data[i] = tmp_target_data[i][index_from_time1:index_from_time2]
            target_data = np.array(target_data)

            fl_metki = "D:\\samples_for_kursach\\metki"
            fl_data = "D:\\samples_for_kursach\\data"

            for i in range(len(target_data)):
                write_data_to_folder_and_metka_to_text(fl_data, fl_metki, target_data[i], type_of_target)

    def load_samples_and_labels(self):
        data_path = "D:\\samples_for_kursach\\data"
        metki_path = "D:\\samples_for_kursach\\metki"
        self.samples, self.labels = load_all_samples_and_labels(data_path, metki_path)
        print("загружено " + str(len(self.samples)) + " примеров")

    def show_signal_and_spectum(self):
        tmp_line = self.lineEdit_16.text()
        i1_for_subplot, i2_for_subplot, number_of_samples = tmp_line.split(';')
        i1 = int(i1_for_subplot)
        i2 = int(i2_for_subplot)
        n = int(number_of_samples)

        index_from_here_we_plot = int(self.lineEdit_15.text())

        plt.clf()

        j = 0  # индекс, отвечающий за правильную метку(идет в титул subplot)
        for i in range(1, n + 1):
            if np.mod(i, 2) != 0:
                self.canvas.axes = self.canvas.fig.add_subplot(i1, i2, i)
                y = self.samples[index_from_here_we_plot + j]
                x = range(len(y))
                self.canvas.plot_linear_signal(x, y)

                self.canvas.axes.set_title(
                    "sample № :  " + str(index_from_here_we_plot + j) + "      label : " + self.labels[
                        index_from_here_we_plot + j])
                print("sample № :  " + str(index_from_here_we_plot + j) + "      label : " + self.labels[
                    index_from_here_we_plot + j])

                self.canvas.axes = self.canvas.fig.add_subplot(i1, i2, i + 1)
                y = get_spectrum(self.samples[index_from_here_we_plot + j])
                x = get_frequencies(self.samples[index_from_here_we_plot + j], 1000)
                self.canvas.plot_linear_signal(x, y)

                self.canvas.axes.set_title(
                    "spectrum of sample № :  " + str(index_from_here_we_plot + j) + "      label : " + self.labels[
                        index_from_here_we_plot + j])
                print("spectrum of sample № :  " + str(index_from_here_we_plot + j) + "      label : " + self.labels[
                    index_from_here_we_plot + j])

                j += 1

    def show_sample(self):

        tmp_line = self.lineEdit_16.text()
        i1_for_subplot, i2_for_subplot, number_of_samples = tmp_line.split(';')
        i1 = int(i1_for_subplot)
        i2 = int(i2_for_subplot)
        n = int(number_of_samples)

        index_from_here_we_plot = int(self.lineEdit_15.text())

        plt.clf()

        j = 0
        for i in range(1, n + 1):
            self.canvas.axes = self.canvas.fig.add_subplot(i1, i2, i)

            y = self.samples[index_from_here_we_plot + j]
            x = range(len(y))
            self.canvas.plot_linear_signal(x, y)

            self.canvas.axes.set_title(
                "sample № :  " + str(index_from_here_we_plot + j) + "      label : " + self.labels[
                    index_from_here_we_plot + j])
            print("sample № :  " + str(index_from_here_we_plot + j) + "      label : " + self.labels[
                index_from_here_we_plot + j])

            j += 1

    def run_training(self):
        training(self.samples, self.labels, self.canvas)

    def write_fixed_sample(self):
        # D:\samples_for_kursach\data
        # D:\samples_for_kursach\metki

        # fixed length of writing sample: for_example 1 sec

        sek = 3
        frame = 1000

        length = sek * frame

        line_of_indeces = self.lineEdit_14.text()
        line_of_times = self.lineEdit_12.text()
        line_of_type = self.lineEdit_13.text()

        index_from_time = time2indeces(line_of_times, 1000)

        type_of_target = line_of_type

        if len(line_of_indeces) <= 2:
            index_of_signal = int(line_of_indeces)  # индекс дорожки в загруженных дорожках
            target_data = self.data_table_FROM_ONE_FILE[index_of_signal][index_from_time:index_from_time + length]

            fl_metki = "D:\\samples_for_kursach\\metki"
            fl_data = "D:\\samples_for_kursach\\data"

            write_data_to_folder_and_metka_to_text(fl_data, fl_metki, target_data, type_of_target)
        else:

            index1, index2 = line_of_indeces.split(";")  # будет записано от  включительно  - до включительно
            index1 = int(index1)
            index2 = int(index2)
            index2 += 1
            tmp_target_data = self.data_table_FROM_ONE_FILE[index1:index2]
            target_data = []
            for i in range(len(tmp_target_data)):
                target_data.append([])
                target_data[i] = tmp_target_data[i][index_from_time:index_from_time + length]
            target_data = np.array(target_data)

            fl_metki = "D:\\samples_for_kursach\\metki"
            fl_data = "D:\\samples_for_kursach\\data"

            for i in range(len(target_data)):
                write_data_to_folder_and_metka_to_text(fl_data, fl_metki, target_data[i], type_of_target)

    def load_filtr(self):
        indeces_of_filtr = self.lineEdit_17.text()
        path = "D:\\samples_for_kursach\\filter_vector"
        self.vec_of_filter = np.load(path + "\\vec_" + indeces_of_filtr + ".npy")
        print('done')
        print(len(self.vec_of_filter))

    def apply_filter(self):

        for i in range(len(self.data_table_FROM_ONE_FILE)):
            length = len(self.vec_of_filter)

            index_of_iterations = 0

            start_index = 0 # данная отметка выставлена с учетом особенности данных

            while start_index + index_of_iterations * length + length  <= len(self.data_table_FROM_ONE_FILE[i]):

                x = self.data_table_FROM_ONE_FILE[i][start_index + index_of_iterations * length :  start_index + index_of_iterations * length + length]
                # real = x / np.linalg.norm(x)
                # imag= np.zeros(len(x))
                real = x
                obraz = np.fft.fft(real)
                obraz *=  self.vec_of_filter
                self.data_table_FROM_ONE_FILE[i][
                start_index + index_of_iterations * length:  start_index + index_of_iterations * length + length] = np.fft.ifft(obraz)


                #непосредственно применение фильтра:
                index_of_iterations +=1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
