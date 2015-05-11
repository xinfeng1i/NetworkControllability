# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from GUI.mainwindowUI import Ui_MainWindow
from GUI.mainwindowUI import my_CentralWidget
from GUI import UIDialog_ER
import sys
import networkx as nx
from threading import Thread
#reload(sys)
#sys.setdefaultencoding('utf-8')


class Dialog_ER(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        QtGui.QDialog.__init__(self, parent)
        
        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Node Number', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)

        grid.addWidget(QtGui.QLabel('Connection Probability', parent=self), 1, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 1, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)

        #spacerItem = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        #layout.addItem(spacerItem)

        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def NumberofNodes(self):
        return self.number_of_nodes.text()

    def ConnectProbability(self):
        return self.connect_probability()

        

class NetworkGUI(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(NetworkGUI, self).__init__(parent)
        self.setupUi(self)
        self.connect_actions()
        self.global_network = nx.Graph()

    def connect_actions(self):
        self.action_exit.triggered.connect(QtGui.qApp.quit)
        self.actionER.triggered.connect(self.generate_ER_network)

    def generate_ER_network(self):
        dialog = QtGui.QDialog()
        ui_dialog = UIDialog_ER.Ui_InputDialog()
        ui_dialog.setupUi(dialog)
        
        node_num = 0
        prob = 0.0
        ok = False
        if dialog.exec_():
            if (ui_dialog.lineEdit_NodeNum.text()).isEmpty() or ui_dialog.lineEdit_ConnectProb.text().isEmpty():
                QtGui.QMessageBox.critical(self, u'参数错误', u'所有参数必须非空 !')
            if not ui_dialog.radioButton.isChecked() and not ui_dialog.radioButton_2.isChecked():
                QtGui.QMessageBox.critical(self, u'参数错误', u'所有参数必须非空 !')

            node_num_str = ui_dialog.lineEdit_NodeNum.text()
            prob_str = ui_dialog.lineEdit_ConnectProb.text()
            (node_num, ok) = node_num_str.toInt()
            #print type(node_num)
            #print node_num
            (prob, ok) = prob_str.toFloat()
            #print prob
            direction = False
            if ui_dialog.radioButton_2.isChecked():
                direction = True
            if node_num < 0 or node_num > 1000:
                QtGui.QMessageBox.critical(self, u'参数错误', u'节点数量必须在 [1, 1000] 之间 !')
            if prob < 0.0 or prob > 1.0:
                QtGui.QMessageBox.critical(self, u'参数错误', u'连接概率必须在 [0, 1] 之间 !')
        dialog.destroy()

        self.global_network.clear()
        self.global_network = nx.erdos_renyi_graph(node_num, prob)
        print self.global_network.number_of_nodes()
        print self.global_network.number_of_edges()
        G=nx.path_graph(10)
        self.centralWidget.update_centralWidget()

        

    def Draw_Network(self):
        nx.draw(self.global_network)

    def main(self):
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = NetworkGUI()
    w.main()
    app.exec_()