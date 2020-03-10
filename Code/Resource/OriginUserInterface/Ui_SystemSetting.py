# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SystemSetting.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SystemSetting(object):
    def setupUi(self, SystemSetting):
        SystemSetting.setObjectName("SystemSetting")
        SystemSetting.resize(400, 333)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SystemSetting)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.downloadpath_label = QtWidgets.QLabel(SystemSetting)
        self.downloadpath_label.setObjectName("downloadpath_label")
        self.horizontalLayout_3.addWidget(self.downloadpath_label)
        self.downloadpath_lineedit = QtWidgets.QLineEdit(SystemSetting)
        self.downloadpath_lineedit.setObjectName("downloadpath_lineedit")
        self.horizontalLayout_3.addWidget(self.downloadpath_lineedit)
        self.downloadpath_toolbutton = QtWidgets.QToolButton(SystemSetting)
        self.downloadpath_toolbutton.setObjectName("downloadpath_toolbutton")
        self.horizontalLayout_3.addWidget(self.downloadpath_toolbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.threads_label = QtWidgets.QLabel(SystemSetting)
        self.threads_label.setObjectName("threads_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.threads_label)
        self.threads_lineedit = QtWidgets.QLineEdit(SystemSetting)
        self.threads_lineedit.setObjectName("threads_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.threads_lineedit)
        self.failedretrytimes_label = QtWidgets.QLabel(SystemSetting)
        self.failedretrytimes_label.setObjectName("failedretrytimes_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.failedretrytimes_label)
        self.failedretrytimes_lineedit = QtWidgets.QLineEdit(SystemSetting)
        self.failedretrytimes_lineedit.setObjectName("failedretrytimes_lineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.failedretrytimes_lineedit)
        self.connecttimeout_label = QtWidgets.QLabel(SystemSetting)
        self.connecttimeout_label.setObjectName("connecttimeout_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.connecttimeout_label)
        self.connecttimeout_lineedit = QtWidgets.QLineEdit(SystemSetting)
        self.connecttimeout_lineedit.setObjectName("connecttimeout_lineedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connecttimeout_lineedit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.header_label = QtWidgets.QLabel(SystemSetting)
        self.header_label.setObjectName("header_label")
        self.gridLayout.addWidget(self.header_label, 0, 0, 1, 1)
        self.header_textedit = QtWidgets.QTextEdit(SystemSetting)
        self.header_textedit.setObjectName("header_textedit")
        self.gridLayout.addWidget(self.header_textedit, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SystemSetting)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SystemSetting)
        QtCore.QMetaObject.connectSlotsByName(SystemSetting)

    def retranslateUi(self, SystemSetting):
        _translate = QtCore.QCoreApplication.translate
        SystemSetting.setWindowTitle(_translate("SystemSetting", "系统设置"))
        self.downloadpath_label.setText(_translate("SystemSetting", "下载路径"))
        self.downloadpath_toolbutton.setText(_translate("SystemSetting", "..."))
        self.threads_label.setText(_translate("SystemSetting", "线程数（并行数量）"))
        self.failedretrytimes_label.setText(_translate("SystemSetting", "失败重复次数"))
        self.connecttimeout_label.setText(_translate("SystemSetting", "连接超时（秒）"))
        self.header_label.setText(_translate("SystemSetting", "定制报头信息      "))


