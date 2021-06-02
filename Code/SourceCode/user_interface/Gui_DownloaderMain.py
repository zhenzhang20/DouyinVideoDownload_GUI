# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_DownloaderMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import Resource.resource_rc

class Gui_DownloaderMain(QMainWindow):
    def setupUi(self):
        self.setObjectName("DownloaderMain")
        self.resize(901, 711)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon(':images/icon/icon.png')
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.URLSettingBtn = QtWidgets.QPushButton(self.centralwidget)
        self.URLSettingBtn.setObjectName("URLSettingBtn")
        self.horizontalLayout_2.addWidget(self.URLSettingBtn)
        self.DownloadResultBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadResultBtn.setObjectName("DownloadResultBtn")
        self.horizontalLayout_2.addWidget(self.DownloadResultBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startdownload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.startdownload_btn.setObjectName("startdownload_btn")
        self.horizontalLayout_3.addWidget(self.startdownload_btn)
        # self.pausedownload_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.pausedownload_btn.setObjectName("pausedownload_btn")
        # self.horizontalLayout_3.addWidget(self.pausedownload_btn)
        # self.stopdownload_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.stopdownload_btn.setObjectName("stopdownload_btn")
        # self.horizontalLayout_3.addWidget(self.stopdownload_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.download_info_table_show = QtWidgets.QTableWidget(self.centralwidget)
        self.download_info_table_show.setObjectName("download_info_table_show")
        self.download_info_table_show.setColumnCount(7)
        self.download_info_table_show.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_info_table_show.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.download_info_table_show)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUser_Config = QtWidgets.QAction(self)
        self.actionUser_Config.setObjectName("actionUser_Config")
        self.actionSystem_Config = QtWidgets.QAction(self)
        self.actionSystem_Config.setObjectName("actionSystem_Config")
        self.actionURL = QtWidgets.QAction(self)
        self.actionURL.setObjectName("actionURL")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionURL)
        self.menuSetting.addAction(self.actionUser_Config)
        self.menuSetting.addAction(self.actionSystem_Config)
        self.menuSetting.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.actionQuit.triggered.connect(self.close)


    def retranslateUi(self, DownloaderMain):
        _translate = QtCore.QCoreApplication.translate
        DownloaderMain.setWindowTitle(_translate("DownloaderMain", "Downloader"))
        self.URLSettingBtn.setText(_translate("DownloaderMain", "URL"))
        self.DownloadResultBtn.setText(_translate("DownloaderMain", "下载结果"))
        self.startdownload_btn.setText(_translate("DownloaderMain", "开始"))
        # self.pausedownload_btn.setText(_translate("DownloaderMain", "暂停"))
        # self.stopdownload_btn.setText(_translate("DownloaderMain", "停止"))
        item = self.download_info_table_show.horizontalHeaderItem(0)
        item.setText(_translate("ConverterMain", "序号"))
        item = self.download_info_table_show.horizontalHeaderItem(1)
        item.setText(_translate("ConverterMain", "主播ID"))
        item = self.download_info_table_show.horizontalHeaderItem(2)
        item.setText(_translate("ConverterMain", "标题"))
        item = self.download_info_table_show.horizontalHeaderItem(3)
        item.setText(_translate("ConverterMain", "状态"))
        item = self.download_info_table_show.horizontalHeaderItem(4)
        item.setText(_translate("ConverterMain", "类型"))
        item = self.download_info_table_show.horizontalHeaderItem(5)
        item.setText(_translate("ConverterMain", "下载时间"))
        item = self.download_info_table_show.horizontalHeaderItem(6)
        item.setText(_translate("ConverterMain", "大小"))
        self.menuFile.setTitle(_translate("DownloaderMain", "File"))
        self.menuEdit.setTitle(_translate("DownloaderMain", "Edit"))
        self.menuSetting.setTitle(_translate("DownloaderMain", "Setting"))
        self.menuHelp.setTitle(_translate("DownloaderMain", "Help"))
        self.actionQuit.setText(_translate("DownloaderMain", "Quit"))
        self.actionAbout.setText(_translate("DownloaderMain", "About"))
        self.actionUser_Config.setText(_translate("DownloaderMain", "User Config"))
        self.actionSystem_Config.setText(_translate("DownloaderMain", "System Config"))
        self.actionURL.setText(_translate("DownloaderMain", "URL"))
