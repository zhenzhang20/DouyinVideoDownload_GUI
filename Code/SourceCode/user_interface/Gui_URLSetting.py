# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_URLSetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import Resource.resource_rc

class Gui_URLSetting(QDialog):

    def setupUi(self):
        self.setObjectName("URLSetting")
        self.resize(818, 455)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon()
        icon = QtGui.QIcon(':images/icon/icon.png')
        self.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.URL = QtWidgets.QLabel(self)
        self.URL.setObjectName("URL")
        self.horizontalLayout.addWidget(self.URL)
        self.url_path = QtWidgets.QLineEdit(self)
        self.url_path.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.url_path)
        self.urlbrowserbutton = QtWidgets.QToolButton(self)
        self.urlbrowserbutton.setObjectName("urlbrowserbutton")
        self.horizontalLayout.addWidget(self.urlbrowserbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.url_table_show = QtWidgets.QTableWidget(self)
        self.url_table_show.setObjectName("url_table_show")
        self.url_table_show.setColumnCount(2)
        self.url_table_show.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.url_table_show.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.url_table_show.setHorizontalHeaderItem(1, item)
        self.url_table_show.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.url_table_show)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, URLSetting):
        _translate = QtCore.QCoreApplication.translate
        URLSetting.setWindowTitle(_translate("URLSetting", "URL 设置"))
        self.URL.setText(_translate("URLSetting", "URL File:"))
        self.urlbrowserbutton.setText(_translate("URLSetting", "..."))
        item = self.url_table_show.horizontalHeaderItem(0)
        item.setText(_translate("URLSetting", "No."))
        item = self.url_table_show.horizontalHeaderItem(1)
        item.setText(_translate("URLSetting", "URL"))

