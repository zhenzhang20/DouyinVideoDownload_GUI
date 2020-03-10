# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_SystemSetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import Resource.resource_rc

class Gui_SystemSetting(QDialog):
    def setupUi(self):
        self.setObjectName("SystemSetting")
        self.resize(400, 333)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon(':images/icon/icon.png')
        self.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.threads_label = QtWidgets.QLabel(self)
        self.threads_label.setObjectName("threads_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.threads_label)
        self.threads_lineedit = QtWidgets.QLineEdit(self)
        self.threads_lineedit.setObjectName("threads_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.threads_lineedit)
        self.failedretrytimes_label = QtWidgets.QLabel(self)
        self.failedretrytimes_label.setObjectName("failedretrytimes_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.failedretrytimes_label)
        self.failedretrytimes_lineedit = QtWidgets.QLineEdit(self)
        self.failedretrytimes_lineedit.setObjectName("failedretrytimes_lineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.failedretrytimes_lineedit)
        self.connecttimeout_label = QtWidgets.QLabel(self)
        self.connecttimeout_label.setObjectName("connecttimeout_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.connecttimeout_label)
        self.connecttimeout_lineedit = QtWidgets.QLineEdit(self)
        self.connecttimeout_lineedit.setObjectName("connecttimeout_lineedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connecttimeout_lineedit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.header_label = QtWidgets.QLabel(self)
        self.header_label.setObjectName("header_label")
        self.gridLayout.addWidget(self.header_label, 0, 0, 1, 1)
        self.header_textedit = QtWidgets.QTextEdit(self)
        self.header_textedit.setObjectName("header_textedit")
        self.gridLayout.addWidget(self.header_textedit, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, SystemSetting):
        _translate = QtCore.QCoreApplication.translate
        SystemSetting.setWindowTitle(_translate("SystemSetting", "系统设置"))
        self.threads_label.setText(_translate("SystemSetting", "线程数（并行数量）"))
        self.failedretrytimes_label.setText(_translate("SystemSetting", "下载失败重复次数"))
        self.connecttimeout_label.setText(_translate("SystemSetting", "连接超时（秒）"))
        self.header_label.setText(_translate("SystemSetting", "定制报头信息      "))

