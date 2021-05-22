# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_prototype.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.possibleNodes = list("ABCDEFGHIJKLMNOPRSTUWXYZ")
        self.possibleNodes.reverse()
        self.graph = nx.DiGraph()




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("background-color: rgb(20, 192, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearNodesBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.clearNodes())
        self.clearNodesBtn.setGeometry(QtCore.QRect(30, 190, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.clearNodesBtn.setFont(font)
        self.clearNodesBtn.setStyleSheet("background-color: rgb(251, 153, 15);color: rgb(36, 46, 56);")
        self.clearNodesBtn.setObjectName("clearNodesBtn")
        self.nodesLabel = QtWidgets.QLabel(self.centralwidget)
        self.nodesLabel.setGeometry(QtCore.QRect(130, 20, 350, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        self.nodesLabel.setFont(font)
        self.nodesLabel.setStyleSheet("color: rgb(36, 46, 56);")
        self.nodesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nodesLabel.setObjectName("nodesLabel")
        self.addNodeBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.addNode())
        self.addNodeBtn.setGeometry(QtCore.QRect(30, 90, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.addNodeBtn.setFont(font)
        self.addNodeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.addNodeBtn.setObjectName("addNodeBtn")
        self.deleteNodeBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.deleteNode())
        self.deleteNodeBtn.setGeometry(QtCore.QRect(30, 140, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.deleteNodeBtn.setFont(font)
        self.deleteNodeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.deleteNodeBtn.setObjectName("deleteNodeBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(590, -60, 21, 771))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.nodesList = QtWidgets.QListWidget(self.centralwidget)
        self.nodesList.setGeometry(QtCore.QRect(220, 90, 321, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nodesList.setFont(font)
        self.nodesList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nodesList.setAutoFillBackground(False)
        self.nodesList.setStyleSheet("background-color: rgb(208, 239, 255);color: rgb(19, 28, 44);")
        self.nodesList.setWordWrap(False)
        self.nodesList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.nodesList.setObjectName("nodesList")
        self.edgesLabel = QtWidgets.QLabel(self.centralwidget)
        self.edgesLabel.setGeometry(QtCore.QRect(130, 290, 350, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        self.edgesLabel.setFont(font)
        self.edgesLabel.setStyleSheet("color: rgb(36, 46, 56);")
        self.edgesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.edgesLabel.setObjectName("edgesLabel")
        self.deleteEdgeBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.deleteEdge())
        self.deleteEdgeBtn.setGeometry(QtCore.QRect(30, 410, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.deleteEdgeBtn.setFont(font)
        self.deleteEdgeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.deleteEdgeBtn.setObjectName("deleteEdgeBtn")
        self.addEdgeBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.addEdge())
        self.addEdgeBtn.setGeometry(QtCore.QRect(420, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.addEdgeBtn.setFont(font)
        self.addEdgeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.addEdgeBtn.setObjectName("addEdgeBtn")
        self.clearEdgesBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.clearEdges())
        self.clearEdgesBtn.setGeometry(QtCore.QRect(300, 410, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.clearEdgesBtn.setFont(font)
        self.clearEdgesBtn.setStyleSheet("background-color: rgb(251, 153, 15);color: rgb(36, 46, 56);")
        self.clearEdgesBtn.setObjectName("clearEdgesBtn")
        self.edgesList = QtWidgets.QListWidget(self.centralwidget)
        self.edgesList.setGeometry(QtCore.QRect(30, 460, 541, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.edgesList.setFont(font)
        self.edgesList.setStyleSheet("background-color: rgb(208, 239, 255);")
        self.edgesList.setObjectName("edgesList")
        self.plotWidget = QtWidgets.QWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(620, 20, 650, 650))
        self.plotWidget.setStyleSheet("background-color: rgb(208, 239, 255);")
        self.plotWidget.setObjectName("plotWidget")
        self.arrowLabel = QtWidgets.QLabel(self.centralwidget)
        self.arrowLabel.setGeometry(QtCore.QRect(190, 370, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.arrowLabel.setFont(font)
        self.arrowLabel.setObjectName("arrowLabel")
        self.sourceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.sourceInput.setGeometry(QtCore.QRect(30, 360, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.sourceInput.setFont(font)
        self.sourceInput.setStyleSheet("background-color: rgb(208, 239, 255);")
        self.sourceInput.setMaxLength(1)
        self.sourceInput.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceInput.setObjectName("sourceInput")
        self.destinationInput = QtWidgets.QLineEdit(self.centralwidget)
        self.destinationInput.setGeometry(QtCore.QRect(270, 360, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.destinationInput.setFont(font)
        self.destinationInput.setStyleSheet("background-color: rgb(208, 239, 255);")
        self.destinationInput.setMaxLength(1)
        self.destinationInput.setAlignment(QtCore.Qt.AlignCenter)
        self.destinationInput.setObjectName("destinationInput")
        self.checkConnectionBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.checkConnection())
        self.checkConnectionBtn.setGeometry(QtCore.QRect(30, 610, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.checkConnectionBtn.setFont(font)
        self.checkConnectionBtn.setStyleSheet("background-color: rgb(228, 72, 45);color: rgb(36, 46, 56);")
        self.checkConnectionBtn.setObjectName("checkConnectionBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sprawdzanie ścisłej spójności grafu skierowanego"))
        self.clearNodesBtn.setText(_translate("MainWindow", "Wyczyść wszystkie"))
        self.nodesLabel.setText(_translate("MainWindow", "Wierzchołki"))
        self.addNodeBtn.setText(_translate("MainWindow", "Dodaj wierzchołek"))
        self.deleteNodeBtn.setText(_translate("MainWindow", "Usuń wierzchołek"))
        self.edgesLabel.setText(_translate("MainWindow", "Krawędzie"))
        self.deleteEdgeBtn.setText(_translate("MainWindow", "Usuń zaznaczoną krawędź"))
        self.addEdgeBtn.setText(_translate("MainWindow", "Dodaj krawędź"))
        self.clearEdgesBtn.setText(_translate("MainWindow", "Wyczyść wszystkie krawędzie"))
        self.arrowLabel.setText(_translate("MainWindow", ">>>>>"))
        self.checkConnectionBtn.setText(_translate("MainWindow", "Sprawdź spójność grafu"))

    def addNode(self):
        if self.nodesList.count() == 24:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Dodano maksymalną liczbę wierzchołków!')
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setWindowFlags(error_dialog.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
            error_dialog.exec_()
            return
        text = self.possibleNodes.pop()
        item = QListWidgetItem(text)
        item.setTextAlignment(Qt.AlignHCenter)
        self.nodesList.addItem(item)
        self.graph.add_node(text)

    def deleteNode(self):
        if self.nodesList.count() == 0 or self.nodesList.currentItem()==None:
            return
        selected = self.nodesList.currentItem()
        self.possibleNodes.append(selected.text())
        self.possibleNodes = sorted(self.possibleNodes,reverse=True)
        self.graph.remove_node(selected.text())
        self.nodesList.takeItem(self.nodesList.row(selected))
        deleteList = []
        for edgeNumber in range(self.edgesList.count()-1,-1,-1):
            edgeText = list(self.edgesList.item(edgeNumber).text())
            if selected.text() in edgeText:
                self.edgesList.takeItem(edgeNumber)
                edgeNumber-=1
                deleteList.append((edgeText[1],edgeText[3]))
        self.graph.remove_edges_from(deleteList)
        print(self.graph.edges)



    def clearNodes(self):
        self.nodesList.clear()
        self.possibleNodes = list("ABCDEFGHIJKLMNOPRSTUWXYZ")
        self.possibleNodes.reverse()
        self.graph.clear()

    def addEdge(self):
        sourceNode = self.sourceInput.text()
        destinationNode = self.destinationInput.text()
        if sourceNode not in list(self.graph.nodes) or destinationNode not in list(self.graph.nodes):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Przynajmniej jeden z podanych wierzchołków nie został dodany do grafu!')
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setWindowFlags(error_dialog.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
            error_dialog.exec_()
            self.sourceInput.setText("")
            self.destinationInput.setText("")
            return
        self.graph.add_edge(sourceNode,destinationNode)
        text = f'({sourceNode},{destinationNode})'
        item = QListWidgetItem(text)
        item.setTextAlignment(Qt.AlignHCenter)
        self.edgesList.addItem(item)
        self.sourceInput.setText("")
        self.destinationInput.setText("")

    def deleteEdge(self):
        if self.edgesList.count() == 0 or self.edgesList.currentItem()==None:
            return
        selected = self.edgesList.currentItem()
        self.edgesList.takeItem(self.edgesList.row(selected))
        self.graph.remove_edges_from([(selected.text()[1],selected.text()[3])])
        print(self.graph.edges)

    def clearEdges(self):
        self.edgesList.clear()
        self.graph.clear_edges()

    def checkConnection(self):
        pos = nx.circular_layout(self.graph, scale=2)  # double distance between all nodes
        nx.draw(self.graph, pos, node_color='yellow', with_labels=True, arrows=True, arrowsize=15)
        plt.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())