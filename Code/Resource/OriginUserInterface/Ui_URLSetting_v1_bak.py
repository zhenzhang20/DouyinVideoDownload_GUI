# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_URLSetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.pushButton_2 = QtWidgets.QPushButton(URLSetting)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(URLSetting)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(URLSetting)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
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
        self.pushButton_2.setText(_translate("URLSetting", "导入"))
        self.pushButton.setText(_translate("URLSetting", "导出"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("URLSetting", "No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("URLSetting", "URL"))
