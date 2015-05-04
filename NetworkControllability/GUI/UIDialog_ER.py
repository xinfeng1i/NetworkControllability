# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIDialog_ER.ui'
#
# Created: Mon May 04 20:56:37 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_InputDialog(object):
    def setupUi(self, InputDialog):
        InputDialog.setObjectName(_fromUtf8("InputDialog"))
        InputDialog.resize(351, 245)
        self.buttonBox = QtGui.QDialogButtonBox(InputDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 200, 391, 31))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(InputDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_NodeNum = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_NodeNum.setObjectName(_fromUtf8("lineEdit_NodeNum"))
        self.gridLayout.addWidget(self.lineEdit_NodeNum, 0, 1, 1, 1)
        self.label_connectProbability = QtGui.QLabel(self.gridLayoutWidget)
        self.label_connectProbability.setMargin(10)
        self.label_connectProbability.setObjectName(_fromUtf8("label_connectProbability"))
        self.gridLayout.addWidget(self.label_connectProbability, 1, 0, 1, 1)
        self.lineEdit_ConnectProb = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ConnectProb.setObjectName(_fromUtf8("lineEdit_ConnectProb"))
        self.gridLayout.addWidget(self.lineEdit_ConnectProb, 1, 1, 1, 1)
        self.label_nodeNum = QtGui.QLabel(self.gridLayoutWidget)
        self.label_nodeNum.setMargin(10)
        self.label_nodeNum.setObjectName(_fromUtf8("label_nodeNum"))
        self.gridLayout.addWidget(self.label_nodeNum, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(InputDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 321, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(100, 20, 61, 19))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 20, 61, 19))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

        self.retranslateUi(InputDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), InputDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), InputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InputDialog)

    def retranslateUi(self, InputDialog):
        InputDialog.setWindowTitle(_translate("InputDialog", "请输入以下参数", None))
        self.label_connectProbability.setText(_translate("InputDialog", "连接概率", None))
        self.label_nodeNum.setText(_translate("InputDialog", "节点数", None))
        self.groupBox.setTitle(_translate("InputDialog", "是否有向", None))
        self.radioButton.setText(_translate("InputDialog", "无向", None))
        self.radioButton_2.setText(_translate("InputDialog", "有向", None))

