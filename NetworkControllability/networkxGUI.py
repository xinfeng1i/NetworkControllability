from PyQt4 import QtGui
from PyQt4 import QtCore
from GUI.mainwindowUI import Ui_MainWindow
import sys

class NetworkGUI(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(NetworkGUI, self).__init__(parent)
        self.setupUi(self)
        self.connect_actions()

    def connect_actions(self):
        self.action_exit.triggered.connect(QtGui.qApp.quit)

    def main(self):
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = NetworkGUI()
    w.main()
    app.exec_()