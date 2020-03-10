# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_URLSetting.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_URLSetting(object):
    def setupUi(self, URLSetting):
        URLSetting.setObjectName("URLSetting")
        URLSetting.resize(818, 455)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(URLSetting)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.URL = QtWidgets.QLabel(URLSetting)
        self.URL.setObjectName("URL")
        self.horizontalLayout.addWidget(self.URL)
        self.url_path = QtWidgets.QLineEdit(URLSetting)
        self.url_path.setObjectName("url_path")
        self.horizontalLayout.addWidget(self.url_path)
        self.URLBrowserButton = QtWidgets.QToolButton(URLSetting)
        self.URLBrowserButton.setObjectName("URLBrowserButton")
        self.horizontalLayout.addWidget(self.URLBrowserButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.url_table_show = QtWidgets.QTableWidget(URLSetting)
        self.url_table_show.setObjectName("url_table_show")
        self.url_table_show.setColumnCount(2)
        self.url_table_show.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.url_table_show.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.url_table_show.setHorizontalHeaderItem(1, item)
        self.url_table_show.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.url_table_show)
        self.buttonBox = QtWidgets.QDialogButtonBox(URLSetting)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(URLSetting)
        QtCore.QMetaObject.connectSlotsByName(URLSetting)

    def retranslateUi(self, URLSetting):
        _translate = QtCore.QCoreApplication.translate
        URLSetting.setWindowTitle(_translate("URLSetting", "URL 设置"))
        self.URL.setText(_translate("URLSetting", "URL File:"))
        self.URLBrowserButton.setText(_translate("URLSetting", "..."))
        item = self.url_table_show.horizontalHeaderItem(0)
        item.setText(_translate("URLSetting", "No."))
        item = self.url_table_show.horizontalHeaderItem(1)
        item.setText(_translate("URLSetting", "URL"))


