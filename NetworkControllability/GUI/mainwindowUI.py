# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowUI.ui'
#
# Created: Mon May 04 16:40:10 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 700)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.file_menu = QtGui.QMenu(self.menubar)
        self.file_menu.setObjectName(_fromUtf8("file_menu"))
        self.network_menu = QtGui.QMenu(self.menubar)
        self.network_menu.setObjectName(_fromUtf8("network_menu"))
        self.centrality_menu = QtGui.QMenu(self.menubar)
        self.centrality_menu.setObjectName(_fromUtf8("centrality_menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_fileopen = QtGui.QAction(MainWindow)
        self.action_fileopen.setObjectName(_fromUtf8("action_fileopen"))
        self.actionER = QtGui.QAction(MainWindow)
        self.actionER.setObjectName(_fromUtf8("actionER"))
        self.actionWS = QtGui.QAction(MainWindow)
        self.actionWS.setObjectName(_fromUtf8("actionWS"))
        self.actionNW = QtGui.QAction(MainWindow)
        self.actionNW.setObjectName(_fromUtf8("actionNW"))
        self.actionSF = QtGui.QAction(MainWindow)
        self.actionSF.setObjectName(_fromUtf8("actionSF"))
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_node_betweeness_centrality = QtGui.QAction(MainWindow)
        self.action_node_betweeness_centrality.setObjectName(_fromUtf8("action_node_betweeness_centrality"))
        self.action_eigenvector_centrality = QtGui.QAction(MainWindow)
        self.action_eigenvector_centrality.setObjectName(_fromUtf8("action_eigenvector_centrality"))
        self.file_menu.addAction(self.action_fileopen)
        self.file_menu.addAction(self.action_exit)
        self.network_menu.addAction(self.actionER)
        self.network_menu.addAction(self.actionWS)
        self.network_menu.addAction(self.actionNW)
        self.network_menu.addAction(self.actionSF)
        self.centrality_menu.addAction(self.action_node_betweeness_centrality)
        self.centrality_menu.addAction(self.action_eigenvector_centrality)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.network_menu.menuAction())
        self.menubar.addAction(self.centrality_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.file_menu.setTitle(_translate("MainWindow", "文件", None))
        self.network_menu.setTitle(_translate("MainWindow", "网络模型", None))
        self.centrality_menu.setTitle(_translate("MainWindow", "中心性", None))
        self.action_fileopen.setText(_translate("MainWindow", "打开", None))
        self.actionER.setText(_translate("MainWindow", "ER随机网络", None))
        self.actionWS.setText(_translate("MainWindow", "WS小世界", None))
        self.actionNW.setText(_translate("MainWindow", "NW小世界", None))
        self.actionSF.setText(_translate("MainWindow", "SF无标度", None))
        self.action_exit.setText(_translate("MainWindow", "退出", None))
        self.action_node_betweeness_centrality.setText(_translate("MainWindow", "介数中心性", None))
        self.action_eigenvector_centrality.setText(_translate("MainWindow", "特征向量中心性 ", None))

