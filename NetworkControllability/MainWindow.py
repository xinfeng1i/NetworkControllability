from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import networkx as nx
import random
import sys
import NetworkModels as NM

GLOBAL_NETWORK = nx.Graph()

class Dialog_ER(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_ER, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Connection Probability p:', parent=self), 1, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 1, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num

    def ConnectProbability(self):
        (prob, ok) = self.connect_probability.text().toFloat()
        return prob

class Dialog_WS(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_WS, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Nearest Neighbors k:', parent=self), 1,0,1,1)
        self.number_of_neighbors = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_neighbors, 1, 1, 1,1)
        grid.addWidget(QtGui.QLabel('Connection Probability p:', parent=self), 2, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 2, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num
    def NumberofNeighbors(self):
        (k, ok) = self.number_of_neighbors.text().toInt()
        return k
    def ConnectProbability(self):
        (prob, ok) = self.connect_probability.text().toFloat()
        return prob

class Dialog_NW(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_NW, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Nearest Neighbors k:', parent=self), 1,0,1,1)
        self.number_of_neighbors = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_neighbors, 1, 1, 1,1)
        grid.addWidget(QtGui.QLabel('Connection Probability p:', parent=self), 2, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 2, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num
    def NumberofNeighbors(self):
        (k, ok) = self.number_of_neighbors.text().toInt()
        return k
    def ConnectProbability(self):
        (prob, ok) = self.connect_probability.text().toFloat()
        return prob

class Dialog_BA(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_BA, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Added Nodes m (m0=m) :', parent=self), 1, 0, 1, 1)
        self.added_nodes_num = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.added_nodes_num, 1, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num

    def NumberofAddedNodes(self):
        (m, ok) = self.added_nodes_num.text().toInt()
        return m

class Dialog_CentralityDisplayResult(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_CentralityDisplayResult, self).__init__(parent)
        self.resize(400, 500)

        grid = QtGui.QGridLayout()
        
        self.edit = QtGui.QTextEdit(self)
        self.buttonBox = QtGui.QDialogButtonBox(parent=self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        btn = QtGui.QPushButton('Plot')
        self.buttonBox.addButton(btn, QtGui.QDialogButtonBox.ActionRole)
        QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), self.plot_function)
        self.column1 = []
        self.column2 = []
        
        grid.addWidget(self.edit, 0, 0, 1, 1)
        grid.addWidget(self.buttonBox, 1, 0, 1, 1)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        self.setLayout(layout)
    def add_contents(self, label1, label2, data_col1, data_col2):
        self.edit.append(label1+'\t'+label2)
        n = len(data_col1)
        for i in range(n):
            self.edit.append("%s\t%f"%(data_col1[i], data_col2[i]))
    def plot_function(self):
        plt.plot(self.column1, self.column2, '-bo')
        plt.show()

class Dialog_EdgeBetCentralityDisplayResult(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_EdgeBetCentralityDisplayResult, self).__init__(parent)
        self.resize(400, 500)

        grid = QtGui.QGridLayout()
        
        self.edit = QtGui.QTextEdit(self)
        self.buttonBox = QtGui.QDialogButtonBox(parent=self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        btn = QtGui.QPushButton('Plot')
        self.buttonBox.addButton(btn, QtGui.QDialogButtonBox.ActionRole)
        QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), self.plot_function)
        self.column1 = []
        self.column2 = []
        
        grid.addWidget(self.edit, 0, 0, 1, 1)
        grid.addWidget(self.buttonBox, 1, 0, 1, 1)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        self.setLayout(layout)
    def add_contents(self, label1, label2, data_col1, data_col2):
        self.edit.append(label1+'\t'+label2)
        n = len(data_col1)
        for i in range(n):
            self.edit.append("%s-%s\t%f"%(data_col1[i][0], data_col1[i][1], data_col2[i]))
    def plot_function(self):
        sz = len(self.column2)
        x = range(sz)
        plt.plot(x, self.column2, '-bo')
        plt.show()


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
        #self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
        pass

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()
    def draw_network(self, G, pos):
        nx.draw(G,pos,ax=self.axes, with_labels=True, font_color='w')
        #nx.draw_networkx_labels(G, pos, ax=self.axes)
        self.draw()

class MyCentralWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyCentralWidget,self).__init__(parent)     
        self.sc = MyDynamicMplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self) 
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.sc)        
        self.setLayout(layout)
    def update_centralWidget(self, G, pos):
        self.sc.draw_network(G, pos)
        

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('Network Controllability Analysis Software')
        self.resize(1000, 800)
        
        #######################################################################################
        # file menu
        #######################################################################################
        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu_open_submenu = QtGui.QMenu("Open")
        self.file_menu_save_submenu = QtGui.QMenu("Save Net As")
        self.file_menu.addMenu(self.file_menu_open_submenu)
        self.file_menu.addMenu(self.file_menu_save_submenu)
        self.file_menu.addAction("Quit", self.file_menu_quit_action)
        self.file_menu_open_submenu.addAction("Pajek File (.net)", self.file_menu_open_pajeknetwork_action)
        self.file_menu_open_submenu.addAction("Graphviz File (.dot)", self.file_menu_open_dotNetwork_action)
        self.file_menu_save_submenu.addAction("Pajek Net (.net)", self.file_menu_save_pajeknetwork_action)
        self.file_menu_save_submenu.addAction("Graphviz File (.dot)", self.file_menu_save_dotNetwork_action)

        self.menuBar().addMenu(self.file_menu)

        #######################################################################################
        # network menu
        #######################################################################################
        self.network_menu = QtGui.QMenu('&Networks', self)

        # regular network
        self.network_menu.addAction('Complete Network', self.network_menu_complete_graph_action)

        # sub-random-network menu
        self.network_menu_random_network_menu = QtGui.QMenu("Random Networks", self.network_menu)
        self.network_menu.addMenu(self.network_menu_random_network_menu)
        self.network_menu_random_network_menu.addAction('ER Network', self.network_menu_ERNetwork_action)
        self.network_menu_random_network_menu.addAction('Directed ER Network', self.directed_network_menu_ERNetwork_action)
       
        # sub-small-world menu
        self.network_menu_smallworld_menu = QtGui.QMenu("Small World Networks", self.network_menu)
        self.network_menu.addMenu(self.network_menu_smallworld_menu)      
        self.network_menu_smallworld_menu.addAction('WS Small World', self.network_menu_WSNetwork_action)
        self.network_menu_smallworld_menu.addAction('Directed WS Small World', self.network_menu_directed_WSNetwork_action)
        self.network_menu_smallworld_menu.addAction('NW Small World', self.network_menu_NWNetwork_action)
        self.network_menu_smallworld_menu.addAction('Directed NW Small World', self.network_menu_directed_NWNetwork_action)
        
        # sub-scale-free menu
        self.network_menu_scale_free_menu = QtGui.QMenu('Scale-Free Networks', self.network_menu)
        self.network_menu.addMenu(self.network_menu_scale_free_menu)
        self.network_menu_scale_free_menu.addAction('BA Scale Free Network', self.network_menu_BANetwork_action)
        self.network_menu_scale_free_menu.addAction('Directed BA Scale Free Network',self.network_menu_directed_BANetwork_action)
        self.network_menu_scale_free_menu.addAction('Parametric Scale Free Network', self.network_menu_SFNetwork_action)

        # sub-real-network menu
        self.network_menu_real_network_menu = QtGui.QMenu("Real Networks", self.network_menu)
        self.network_menu.addMenu(self.network_menu_real_network_menu)
        self.network_menu_real_network_menu.addAction('Karate Club Network', self.network_menu_karate_club_network_action)
        self.menuBar().addMenu(self.network_menu)

        ###############################################################################################
        # Features menu
        ###############################################################################################
        self.feature_menu = QtGui.QMenu("Features", self)
        self.feature_menu.addAction("Degree Distribution", self.feature_menu_degree_action)
        self.feature_menu.addAction("Clustering Coefficients", self.feature_menu_clusteringcoefficient_action)
        self.feature_menu.addAction("Diameter", self.feature_menu_diameter_action)
        self.menuBar().addMenu(self.feature_menu)

        ###############################################################################################
        # centrality menu
        ###############################################################################################
        self.centrality_menu = QtGui.QMenu('&Centrality', self)
        self.centrality_menu.addAction('Degree Centrality', self.centrality_menu_NodeDegree_action)
        self.centrality_menu.addAction('Betweenness Centrality', self.centrality_menu_NodeBetweenness_action)
        self.centrality_menu.addAction('Edge Betweenness Centrality', self.centrality_menu_EdgeBetweenness_action)
        self.centrality_menu.addAction('Closeness Centrality', self.centrality_menu_ClosenessBetweenness_action)
        self.centrality_menu.addAction('Eigenvector Centrality', self.centrality_menu_EigenvectorBetweenness_action)
        self.centrality_menu.addSeparator()
        self.centrality_menu.addAction('Current-flow Betweenness Centrality', self.centrality_menu_CurrentFlowBetweennessCentrality_action)
        self.centrality_menu.addAction('Current-flow Closeness Centrality', self.centrality_menu_CurrentFlowClosenessCentrality_action)
        self.centrality_menu.addSeparator()
        self.centrality_menu.addAction('Katz Centrality', self.centrality_menu_KatzCentrality_action)
        self.centrality_menu.addSeparator()
        self.centrality_menu.addAction('Load Centrality', self.centrality_menu_LoadCentrality_action)
        self.menuBar().addMenu(self.centrality_menu)

        ##############################################################################################
        # controllability menu
        ##############################################################################################
        self.controllability_menu = QtGui.QMenu('&Controllability', self)
        self.controllability_menu.addAction('Structral Controllability', self.controllability_menu_StructralControllability_action)
        self.controllability_menu.addAction('Exact Controllability', self.controllability_menu_ExactControllability_action)
        self.menuBar().addMenu(self.controllability_menu)

        ###############################################################################################
        # Robustness menu
        ###############################################################################################
        self.robustness_menu = QtGui.QMenu('&Robustness', self)
        self.robustness_menu.addAction('Random Attack', self.robustness_menu_RondomAttack_action)
        self.robustness_menu.addAction('Recalculated Max-Degree Attack', self.robustness_menu_RecaculatedMaxDegree_action)
        self.robustness_menu.addAction('Recalculated Max-Betweenness Attack', self.robustness_menu_RecaculatedMaxBetweenness_action)
        self.robustness_menu.addAction('Cascaded Attack based on Node-Capacity', self.robustness_menu_CascadeBasedonNodeCapacity_action)
        self.menuBar().addMenu(self.robustness_menu)

        ##############################################################################################
        # Draw Menu
        ##############################################################################################
        self.draw_menu = QtGui.QMenu("&Draw", self)
        self.draw_menu_layout_submenu = QtGui.QMenu("Layouts", self.draw_menu)
        self.draw_menu.addMenu(self.draw_menu_layout_submenu)
        self.draw_menu_layout_submenu.addAction("Circle Layout", self.draw_menu_circleLayout_action)
        self.draw_menu_layout_submenu.addAction("Random Layout", self.draw_menu_randomLayout_action)
        self.draw_menu_layout_submenu.addAction("Shell Layout", self.draw_menu_shellLayout_action)
        self.draw_menu_layout_submenu.addAction("Spring Layout", self.draw_menu_springLayout_action)
        self.draw_menu_layout_submenu.addAction("Spectral Layout", self.draw_menu_spectralLayout_action)

        self.menuBar().addMenu(self.draw_menu)


        # about menu
        self.about_menu = QtGui.QMenu('&About', self)
        self.about_menu.addAction('Network Info', self.about_menu_aboutNetwork_action)
        self.about_menu.addAction('About', self.about_menu_About_action)
        self.menuBar().addMenu(self.about_menu)

        # status bar
        #self.statusbar = QtGui.QStatusBar(self)
        self.statusBar().showMessage(nx.info(GLOBAL_NETWORK))

        # central Widget
        self.main_widget = MyCentralWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        G=nx.path_graph(10)
        pos=nx.spring_layout(G)
        self.main_widget.update_centralWidget(G, pos)
   
    ##################################################################
    # 
    # File Menu Actions
    # 
    ##################################################################
    
    # open pajek
    def file_menu_open_pajeknetwork_action(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open Pajek (.net) file", "./Nets", "Pajek Files (*.net)")
        filename = str(filename.toUtf8())
        if filename:            
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.read_pajek(filename)
            if GLOBAL_NETWORK.is_multigraph():
                if GLOBAL_NETWORK.is_directed():
                    GLOBAL_NETWORK = nx.DiGraph(GLOBAL_NETWORK)
                else:
                    GLOBAL_NETWORK = nx.Graph(GLOBAL_NETWORK)
            pos = nx.layout.circular_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)
        else:
            return

    # save pajek
    def file_menu_save_pajeknetwork_action(self):
        # valid check, empty network no needed to be saved
        global GLOBAL_NETWORK
        if (not GLOBAL_NETWORK.nodes()) and (not GLOBAL_NETWORK.edges()):
            QtGui.QMessageBox.warning(self, "Warning", "There is no Networks to Save !")
            return
        # save files
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save as...", "./Nets", "Pajek Files (*.net)")
        filename = str(filename.toUtf8())
        if filename:
            nx.write_pajek(GLOBAL_NETWORK, filename)
            QtGui.QMessageBox.information(self, "title", "Save Net Files Successfully !")
        else:
            pass
    
    # open graphviz net
    def file_menu_open_dotNetwork_action(self):
        QtGui.QMessageBox.information(self, "Info", "Developing..., will come back soon")
    
    # save graphviz net
    def file_menu_save_dotNetwork_action(self):
        # valid check, empty network no needed to be saved
        global GLOBAL_NETWORK
        if (not GLOBAL_NETWORK.nodes()) and (not GLOBAL_NETWORK.edges()):
            QtGui.QMessageBox.warning(self, "Warning", "There is no Networks to Save !")
            return
        # save files
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save as...", "./Nets", "Graphviz Files (*.dot)")
        filename = str(filename.toUtf8())
        if filename:
            nx.write_pajek(GLOBAL_NETWORK, filename)
            QtGui.QMessageBox.information(self, "title", "Save Net Files Successfully !")
        else:
            pass

    def file_menu_quit_action(self):
        QtGui.qApp.exit()

    ##################################################################
    # 
    # Network Models Actions
    # 
    ##################################################################
    def network_menu_complete_graph_action(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input The Parameter', 'Node Num N:')
        if ok:
            n = int(text)
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.complete_graph(n)
            pos = nx.layout.circular_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    def network_menu_ERNetwork_action(self):
        dialog = Dialog_ER(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            p = dialog.ConnectProbability()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if p <= 0.0 or p >= 1.0:
                QtGui.QMessageBox.critical(self, "ERROR", "p must be a float number in (0.0, 1.0)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.erdos_renyi_graph(n, p)
            pos = nx.spring_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def directed_network_menu_ERNetwork_action(self):
        dialog = Dialog_ER(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            p = dialog.ConnectProbability()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if p <= 0.0 or p >= 1.0:
                QtGui.QMessageBox.critical(self, "ERROR", "p must be a float number in (0.0, 1.0)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.erdos_renyi_graph(n, p, directed=True)
            pos = nx.spectral_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)
    
    def network_menu_WSNetwork_action(self):
        dialog = Dialog_WS(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            k = dialog.NumberofNeighbors()
            p = dialog.ConnectProbability()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if k % 2 == 1:
                QtGui.QMessageBox.critical(self, "ERROR", "k must be an even number & k < n")
                return
            if p <= 0.0 or p >= 1.0:
                QtGui.QMessageBox.critical(self, "ERROR", "p must be a float number in (0.0, 1.0)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.watts_strogatz_graph(n, k, p)
            pos = nx.layout.circular_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_directed_WSNetwork_action(self):
        dialog = Dialog_WS(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            k = dialog.NumberofNeighbors()
            p = dialog.ConnectProbability()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if k % 2 == 1:
                QtGui.QMessageBox.critical(self, "ERROR", "k must be an even number & k < n")
                return
            if p <= 0.0 or p >= 1.0:
                QtGui.QMessageBox.critical(self, "ERROR", "p must be a float number in (0.0, 1.0)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = NM.directed_watts_strogatz_graph(n,k,p)
            pos = nx.layout.circular_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_NWNetwork_action(self):
        dialog = Dialog_NW(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            k = dialog.NumberofNeighbors()
            p = dialog.ConnectProbability()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if k % 2 == 1:
                QtGui.QMessageBox.critical(self, "ERROR", "k must be an even number & k < n")
                return
            if p <= 0.0 or p >= 1.0:
                QtGui.QMessageBox.critical(self, "ERROR", "p must be a float number in (0.0, 1.0)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.newman_watts_strogatz_graph(n, k, p)
            pos = nx.layout.circular_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_directed_NWNetwork_action(self):
        dialog = Dialog_NW(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            k = dialog.NumberofNeighbors()
            p = dialog.ConnectProbability()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if k % 2 == 1:
                QtGui.QMessageBox.critical(self, "ERROR", "k must be an even number & k < n")
                return
            if p <= 0.0 or p >= 1.0:
                QtGui.QMessageBox.critical(self, "ERROR", "p must be a float number in (0.0, 1.0)")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = NM.directed_newman_watts_strogatz_graph(n,k,p)
            pos = nx.layout.circular_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    def network_menu_BANetwork_action(self):
        dialog = Dialog_BA(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            m = dialog.NumberofAddedNodes()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if m > n:
                QtGui.QMessageBox.critical(self, "ERROR", "added nodes must has m < n")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = nx.barabasi_albert_graph(n, m)
            pos = nx.layout.spring_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_directed_BANetwork_action(self):
        dialog = Dialog_BA(self)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            n = dialog.NumberofNodes()
            m = dialog.NumberofAddedNodes()
            if n <= 0 or n >= 1000:
                QtGui.QMessageBox.critical(self, "ERROR", "N must be an integer in (0, 1000)")
                return
            if m > n:
                QtGui.QMessageBox.critical(self, "ERROR", "added nodes must has m < n")
                return
            global GLOBAL_NETWORK
            GLOBAL_NETWORK.clear()
            GLOBAL_NETWORK = NM.directed_barabasi_albert_graph(n, m)
            pos = nx.layout.spring_layout(GLOBAL_NETWORK)
            self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    def network_menu_SFNetwork_action(self):
        pass

    def network_menu_karate_club_network_action(self):
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.karate_club_graph()
        pos = nx.layout.spring_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    ##############################################################################
    # 
    # Features (degree & degree distribution, betweenness, closeness, eigenvector)
    # 
    ###############################################################################
    def feature_menu_degree_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('degree distribution')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.degree(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.column1 = col1
        dialog.column2 = col2
        dialog.add_contents('NodeID', 'Degree', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/features/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId Degree'
                    for i in range(len(col1)):
                        print >> fp, '%s %d'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass

    def feature_menu_clusteringcoefficient_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('clustering coefficient distribution')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.clustering(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.column1 = col1
        dialog.column2 = col2
        dialog.add_contents('NodeID', 'Clustering Coefficient', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/features/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId ClusteringCoefficient'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass
        

    def feature_menu_diameter_action(self):
        global GLOBAL_NETWORK
        d = nx.diameter(GLOBAL_NETWORK)
        QtGui.QMessageBox.about(self, "Prompt", "The Network Diameter is %d" %(d))  





    ##################################################################
    # 
    # Centrality (degree, betweenness, closeness, eigenvector) Actions
    # 
    ##################################################################

    def centrality_menu_NodeDegree_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('node degree centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.degree_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.column1 = col1
        dialog.column2 = col2
        dialog.add_contents('NodeID', 'Degree Centrality', col1, col2)        
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId DegreeCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass


    def centrality_menu_NodeBetweenness_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('node betweenness centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.betweenness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.column1 = col1
        dialog.column2 = col2
        dialog.add_contents('NodeID', 'Betweenness Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId BetweennessCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass

    def centrality_menu_EdgeBetweenness_action(self):
        dialog = Dialog_EdgeBetCentralityDisplayResult(self)
        dialog.setWindowTitle('edge betweenness centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for (u, v), y in nx.edge_betweenness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append((u, v))
            col2.append(y)
        dialog.column1 = col1
        dialog.column2 = col2
        dialog.add_contents('edge', 'edge betweenness centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'Edge EdgeBetweennessCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s-%s %f'%(col1[i][0],col1[i][1], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass


    def centrality_menu_ClosenessBetweenness_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('node closeness centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        dialog.column1 = col1
        dialog.column2 = col2
        global GLOBAL_NETWORK
        for x, y in nx.closeness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Closeness Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId ClosenessCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass


    def centrality_menu_EigenvectorBetweenness_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        dialog.setWindowTitle('node eigenvector centrality')
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.eigenvector_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.column1 = col1
        dialog.column2 = col2
        dialog.add_contents('NodeID', 'Eigenvector Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId EigenvectorCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass

    def centrality_menu_CurrentFlowBetweennessCentrality_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('node current-flow betweenness centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        dialog.column1 = col1
        dialog.column2 = col2
        global GLOBAL_NETWORK
        for x, y in nx.current_flow_betweenness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Current-flow Betweenness Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId CurrentFlowBetweennessCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass

    def centrality_menu_CurrentFlowClosenessCentrality_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('node current-flow closeness centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        dialog.column1 = col1
        dialog.column2 = col2
        global GLOBAL_NETWORK
        for x, y in nx.current_flow_closeness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Current-flow Closeness Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId CurrentFlowClosenessCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass

    def centrality_menu_KatzCentrality_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('katz centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        dialog.column1 = col1
        dialog.column2 = col2
        global GLOBAL_NETWORK
        for x, y in nx.katz.katz_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Katz Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId KatzCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass
    
    def centrality_menu_LoadCentrality_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        dialog.setWindowTitle('load centrality')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Save')
        dialog.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Close')
        col1 = []
        col2 = []
        dialog.column1 = col1
        dialog.column2 = col2
        global GLOBAL_NETWORK
        for x, y in nx.load_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Load Centrality', col1, col2)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file to', './results/centrality/', "Text Files (*.txt)")
            if fname:
                with open(fname, 'w') as fp:
                    print >> fp, 'NodeId LoadCentrality'
                    for i in range(len(col1)):
                        print >> fp, '%s %f'%(col1[i], col2[i])
                QtGui.QMessageBox.information(self, 'Message', 'Save Successfully !')
        else:
            pass


    def controllability_menu_StructralControllability_action(self):
        pass
    def controllability_menu_ExactControllability_action(self):
        pass

    def robustness_menu_RondomAttack_action(self):
        pass
    def robustness_menu_RecaculatedMaxDegree_action(self):
        pass
    def robustness_menu_RecaculatedMaxBetweenness_action(self):
        pass
    def robustness_menu_CascadeBasedonNodeCapacity_action(self):
        pass


    ##################################################################
    # 
    # Draw Actions (Layout)
    # 
    ##################################################################
    def draw_menu_circleLayout_action(self):
        global GLOBAL_NETWORK
        pos = nx.layout.circular_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)
        
    def draw_menu_randomLayout_action(self):
        global GLOBAL_NETWORK
        pos = nx.layout.random_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def draw_menu_shellLayout_action(self):
        global GLOBAL_NETWORK
        pos = nx.layout.shell_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def draw_menu_springLayout_action(self):
        global GLOBAL_NETWORK
        pos = nx.layout.spring_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def draw_menu_spectralLayout_action(self):
        global GLOBAL_NETWORK
        pos = nx.layout.spectral_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def about_menu_About_action(self):
        QtGui.QMessageBox.about(self, "About",
        """
        Network Controllability Analysis Software

        Copyright (C) 2015 Xin-Feng Li (silfer.lee@gmail.com)

        This program is distributed under BSD License
        """)
        
    def about_menu_aboutNetwork_action(self):
        global GLOBAL_NETWORK
        s = nx.info(GLOBAL_NETWORK)
        QtGui.QMessageBox.about(self, "Basic Network Info", s)        

if __name__ == "__main__":
    qApp = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(qApp.exec_())