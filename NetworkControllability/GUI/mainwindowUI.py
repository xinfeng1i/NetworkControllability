# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowUI.ui'
#
# Created: Mon May 04 16:40:10 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import networkx as nx
import random

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

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass



class MyStaticMplCanvas(MyMplCanvas):
    def compute_initial_figure(self):
        G=nx.path_graph(10)
        pos=nx.spring_layout(G)
        nx.draw(G,pos,ax=self.axes)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        #timer = QtCore.QTimer(self)
        #timer.timeout.connect(self.update_figure)
        #timer.start(1000)
        #self.update_figure()
        #self.draw_network()

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()
    def draw_network(self, G):
        #G=nx.path_graph(10)
        pos=nx.spring_layout(G)
        nx.draw(G,pos,ax=self.axes)


class my_CentralWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(my_CentralWidget,self).__init__(parent)     
        self.sc = MyDynamicMplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self) 
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.sc)        
        self.setLayout(layout)
    def update_centralWidget(self):
        pass
         

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 700)
        #self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget = my_CentralWidget(MainWindow)
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

