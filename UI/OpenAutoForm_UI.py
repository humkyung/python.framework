# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\OpenAutoForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenAutoFormDialog(object):
    def setupUi(self, OpenAutoFormDialog):
        OpenAutoFormDialog.setObjectName("OpenAutoFormDialog")
        OpenAutoFormDialog.resize(673, 137)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/AViewer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OpenAutoFormDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(OpenAutoFormDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(OpenAutoFormDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditNodes = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNodes.setObjectName("lineEditNodes")
        self.horizontalLayout.addWidget(self.lineEditNodes)
        self.toolButtonNodefile = QtWidgets.QToolButton(self.groupBox)
        self.toolButtonNodefile.setObjectName("toolButtonNodefile")
        self.horizontalLayout.addWidget(self.toolButtonNodefile)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditElements = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditElements.setObjectName("lineEditElements")
        self.horizontalLayout_2.addWidget(self.lineEditElements)
        self.toolButtonElementfile = QtWidgets.QToolButton(self.groupBox)
        self.toolButtonElementfile.setObjectName("toolButtonElementfile")
        self.horizontalLayout_2.addWidget(self.toolButtonElementfile)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenAutoFormDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(OpenAutoFormDialog)
        self.buttonBox.accepted.connect(OpenAutoFormDialog.accept)
        self.buttonBox.rejected.connect(OpenAutoFormDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenAutoFormDialog)

    def retranslateUi(self, OpenAutoFormDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenAutoFormDialog.setWindowTitle(_translate("OpenAutoFormDialog", "Open Dialog"))
        self.groupBox.setTitle(_translate("OpenAutoFormDialog", "Select files"))
        self.toolButtonNodefile.setText(_translate("OpenAutoFormDialog", "..."))
        self.label.setText(_translate("OpenAutoFormDialog", "Node file : "))
        self.label_2.setText(_translate("OpenAutoFormDialog", "Element file : "))
        self.toolButtonElementfile.setText(_translate("OpenAutoFormDialog", "..."))
import Resource_rc
