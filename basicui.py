# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1250, 288)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1231, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelHDKPath = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelHDKPath.setObjectName("labelHDKPath")
        self.horizontalLayout.addWidget(self.labelHDKPath)
        self.lineEditHDKPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditHDKPath.setObjectName("lineEditHDKPath")
        self.horizontalLayout.addWidget(self.lineEditHDKPath)
        self.pushButtonHDKPathOpen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonHDKPathOpen.setObjectName("pushButtonHDKPathOpen")
        self.horizontalLayout.addWidget(self.pushButtonHDKPathOpen)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 1231, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelHoudiniPath = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelHoudiniPath.setObjectName("labelHoudiniPath")
        self.horizontalLayout_2.addWidget(self.labelHoudiniPath)
        self.lineEditHoudiniPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditHoudiniPath.setObjectName("lineEditHoudiniPath")
        self.horizontalLayout_2.addWidget(self.lineEditHoudiniPath)
        self.pushButtonHoudiniPathOpen = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonHoudiniPathOpen.setObjectName("pushButtonHoudiniPathOpen")
        self.horizontalLayout_2.addWidget(self.pushButtonHoudiniPathOpen)
        self.comboBoxVisualStudio = QtWidgets.QComboBox(Widget)
        self.comboBoxVisualStudio.setGeometry(QtCore.QRect(850, 190, 271, 31))
        self.comboBoxVisualStudio.setObjectName("comboBoxVisualStudio")
        self.comboBoxVisualStudio.addItem("")
        self.pushButtonProjectBuild = QtWidgets.QPushButton(Widget)
        self.pushButtonProjectBuild.setGeometry(QtCore.QRect(1150, 190, 91, 31))
        self.pushButtonProjectBuild.setObjectName("pushButtonProjectBuild")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelHDKPath.setText(_translate("Widget", "HDK Project Path: "))
        self.pushButtonHDKPathOpen.setText(_translate("Widget", "Open"))
        self.labelHoudiniPath.setText(_translate("Widget", "Houdini Path:     "))
        self.pushButtonHoudiniPathOpen.setText(_translate("Widget", "Open"))
        self.comboBoxVisualStudio.setItemText(0, _translate("Widget", "Visual Studio 15 2017 x64"))
        self.pushButtonProjectBuild.setText(_translate("Widget", "    Build    "))
