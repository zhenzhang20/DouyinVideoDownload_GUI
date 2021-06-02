# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_SystemSetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import Resource.resource_rc

class Gui_UserSetting(QDialog):
    def setupUi(self):
        self.setObjectName("UserSetting")
        self.resize(400, 133)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon(':images/icon/icon.png')
        self.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.downloadpath_label = QtWidgets.QLabel(self)
        self.downloadpath_label.setObjectName("downloadpath_label")
        self.horizontalLayout_3.addWidget(self.downloadpath_label)
        self.downloadpath_lineedit = QtWidgets.QLineEdit(self)
        self.downloadpath_lineedit.setObjectName("downloadpath_lineedit")
        self.horizontalLayout_3.addWidget(self.downloadpath_lineedit)
        self.downloadpathbrowserbutton = QtWidgets.QToolButton(self)
        self.downloadpathbrowserbutton.setObjectName("downloadpathbrowserbutton")
        self.horizontalLayout_3.addWidget(self.downloadpathbrowserbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.namingrule_label = QtWidgets.QLabel(self)
        self.namingrule_label.setScaledContents(False)
        self.namingrule_label.setObjectName("namingrule_label")
        self.horizontalLayout_4.addWidget(self.namingrule_label)
        self.namingrule_combobox = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.namingrule_combobox.sizePolicy().hasHeightForWidth())
        self.namingrule_combobox.setSizePolicy(sizePolicy)
        self.namingrule_combobox.setObjectName("namingrule_combobox")
        self.horizontalLayout_4.addWidget(self.namingrule_combobox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.md5_label = QtWidgets.QLabel(self)
        self.md5_label.setObjectName("md5_label")
        self.horizontalLayout.addWidget(self.md5_label)
        self.md5_combobox = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.md5_combobox.sizePolicy().hasHeightForWidth())
        self.md5_combobox.setSizePolicy(sizePolicy)
        self.md5_combobox.setObjectName("md5_comboBox")
        self.horizontalLayout.addWidget(self.md5_combobox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.trailerpicture_label = QtWidgets.QLabel(self)
        self.trailerpicture_label.setObjectName("trailerpicture_label")
        self.horizontalLayout_5.addWidget(self.trailerpicture_label)
        self.trailerpicture_lineedit = QtWidgets.QLineEdit(self)
        self.trailerpicture_lineedit.setObjectName("trailerpicture_lineedit")
        self.horizontalLayout_5.addWidget(self.trailerpicture_lineedit)
        self.trailerpicturebrowserbutton = QtWidgets.QToolButton(self)
        self.trailerpicturebrowserbutton.setObjectName("trailerpicturebrowserbutton")
        self.horizontalLayout_5.addWidget(self.trailerpicturebrowserbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.trailervideo_label = QtWidgets.QLabel(self)
        self.trailervideo_label.setObjectName("trailervideo_label")
        self.horizontalLayout_6.addWidget(self.trailervideo_label)
        self.trailervideo_lineedit = QtWidgets.QLineEdit(self)
        self.trailervideo_lineedit.setObjectName("trailervideo_lineedit")
        self.horizontalLayout_6.addWidget(self.trailervideo_lineedit)
        self.trailervideobrowserbutton = QtWidgets.QToolButton(self)
        self.trailervideobrowserbutton.setObjectName("trailervideobrowserbutton")
        self.horizontalLayout_6.addWidget(self.trailervideobrowserbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, UserSetting):
        _translate = QtCore.QCoreApplication.translate
        UserSetting.setWindowTitle(_translate("UserSetting", "用户设置"))
        self.downloadpath_label.setText(_translate("UserSetting", "下载路径    "))
        self.downloadpathbrowserbutton.setText(_translate("UserSetting", "..."))
        self.namingrule_label.setText(_translate("UserSetting", "文件名规则  "))
        self.md5_label.setText(_translate("UserSetting", "MD5修改     "))
        self.trailerpicture_label.setText(_translate("UserSetting", "片尾图片路径"))
        self.trailerpicturebrowserbutton.setText(_translate("UserSetting", "..."))
        self.trailervideo_label.setText(_translate("UserSetting", "片尾视频路径"))
        self.trailervideobrowserbutton.setText(_translate("UserSetting", "..."))
