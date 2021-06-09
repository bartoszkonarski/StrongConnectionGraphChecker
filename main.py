from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from algorithm import Graph, isGraphStronglyConnected

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=500, height=500, dpi=100, graph=None):
        self.fig = Figure(figsize=(width, height),
                          dpi=dpi)
        self.axes = self.fig.add_subplot(
            111)
        self.graph = graph
        self.plot()
        self.parent = parent
        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        pos = nx.circular_layout(self.graph, scale=2)
        nx.draw(self.graph, pos, node_color='orange', with_labels=True, arrows=True, arrowsize=15,edgecolors='black', ax=self.axes)



class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.possibleNodes = list("ABCDEFGHIJKLMNOPRSTUWXYZ")
        self.possibleNodes.reverse()
        self.graph = nx.DiGraph()



    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("background-color: rgb(20, 192, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearNodesBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clearNodes())
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
        self.addNodeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addNode())
        self.addNodeBtn.setGeometry(QtCore.QRect(30, 90, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.addNodeBtn.setFont(font)
        self.addNodeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.addNodeBtn.setObjectName("addNodeBtn")
        self.deleteNodeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.deleteNode())
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
        self.deleteEdgeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.deleteEdge())
        self.deleteEdgeBtn.setGeometry(QtCore.QRect(30, 410, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.deleteEdgeBtn.setFont(font)
        self.deleteEdgeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.deleteEdgeBtn.setObjectName("deleteEdgeBtn")
        self.addEdgeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addEdge())
        self.addEdgeBtn.setGeometry(QtCore.QRect(420, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.addEdgeBtn.setFont(font)
        self.addEdgeBtn.setStyleSheet("background-color: rgb(234, 196, 61);color: rgb(36, 46, 56);")
        self.addEdgeBtn.setObjectName("addEdgeBtn")
        self.clearEdgesBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clearEdges())
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
        self.plotWidget = PlotCanvas(self.centralwidget, graph=self.graph)
        self.plotWidget.setGeometry(QtCore.QRect(620, 20, 650, 650))

        self.plotWidget.setObjectName("plotWidget")
        self.infoWidget = QtWidgets.QTextEdit(self.plotWidget)
        self.infoWidget.setGeometry(QtCore.QRect(0, 0, 650, 650))
        self.infoWidget.setObjectName("infoWidget")
        self.infoWidget.setStyleSheet("background-color: rgb(208, 239, 255);")
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
        self.checkConnectionBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.checkConnection())
        self.checkConnectionBtn.setGeometry(QtCore.QRect(30, 610, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.checkConnectionBtn.setFont(font)
        self.checkConnectionBtn.setStyleSheet("background-color: rgb(228, 72, 45);color: rgb(36, 46, 56);")
        self.checkConnectionBtn.setObjectName("checkConnectionBtn")
        self.infoBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.toggleInfo())
        self.infoBtn.setGeometry(QtCore.QRect(30, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.infoBtn.setFont(font)
        self.infoBtn.setStyleSheet("color: rgb(36, 46, 56);background-color: rgb(252, 255, 20);")
        self.infoBtn.setObjectName("infoBtn")
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
        self.infoWidget.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" margin-right:15px;margin-left:15px;font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:100px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">Aplikacja do badania spójności grafu skierowanego</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Autorzy:</span><span style=\" font-size:14pt; font-weight:600;\"> </span><span style=\" font-size:14pt;\">Cezary Czarnogłowski, Cezary Olender, Bartosz Konarski </span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline;\">Instrukcja obsługi:</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">1. Aby rozpocząć tworzenie grafu, należy dodać interesującą nas liczbę wierzchołków, wierzchołki otrzymują jako etykiety kolejne litery alfabetu. W razie pomyłki możliwe jest zaznaczenie wierzchołka z listy i usunięcie go odpowiednim przyciskiem</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">2. Następnie należy przystąpić do dodania krawędzi pomiędzy istniejącymi wierzchołkami. W tym celu podajemy litery interesujących nas wierzchołków i dodajemy krawędź odpowiednim przyciskiem</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">3. Po dodaniu interesujących nas krawędzi, można uruchomić algorytm sprawdzający spójność grafu przyciskiem: &quot;Sprawdź spójność grafu&quot;</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Po prawej stronie (w miejscu tej instrukcji) przez cały czas dostępny będzie aktualny podgląd grafu ułatwiający pracę z nim.</span></p></body></html>"))
        self.arrowLabel.setText(_translate("MainWindow", ">>>>>"))
        self.arrowLabel.setText(_translate("MainWindow", ">>>>>"))
        self.checkConnectionBtn.setText(_translate("MainWindow", "Sprawdź spójność grafu"))
        self.infoBtn.setText(_translate("MainWindow", "Instrukcja"))

    def addNode(self):
        if self.nodesList.count() == 24:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Dodano maksymalną liczbę wierzchołków!')
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setWindowFlags(error_dialog.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
            error_dialog.exec_()
            return
        text = self.possibleNodes.pop()
        self.graph.add_node(text)
        self.updateGraph()


    def deleteNode(self):
        if self.nodesList.count() == 0 or self.nodesList.currentItem() == None:
            return
        selected = self.nodesList.currentItem()
        self.possibleNodes.append(selected.text())
        self.possibleNodes = sorted(self.possibleNodes, reverse=True)
        self.graph.remove_node(selected.text())
        self.nodesList.takeItem(self.nodesList.row(selected))
        deleteList = []
        for edgeNumber in range(self.edgesList.count() - 1, -1, -1):
            edgeText = list(self.edgesList.item(edgeNumber).text())
            if selected.text() in edgeText:
                self.edgesList.takeItem(edgeNumber)
                edgeNumber -= 1
                deleteList.append((edgeText[1], edgeText[3]))
        self.graph.remove_edges_from(deleteList)
        self.updateGraph()

    def clearNodes(self):
        self.possibleNodes = list("ABCDEFGHIJKLMNOPRSTUWXYZ")
        self.possibleNodes.reverse()
        self.graph.clear()
        self.updateGraph()

    def addEdge(self):
        sourceNode = self.sourceInput.text().upper()
        destinationNode = self.destinationInput.text().upper()
        if sourceNode not in list(self.graph.nodes) or destinationNode not in list(self.graph.nodes):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Przynajmniej jeden z podanych wierzchołków nie został dodany do grafu!')
            error_dialog.setWindowTitle('Błąd')
            error_dialog.setWindowFlags(error_dialog.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
            error_dialog.exec_()
            return
        self.graph.add_edge(sourceNode, destinationNode)
        self.updateGraph()
        self.infoWidget.hide()

    def deleteEdge(self):
        if self.edgesList.count() == 0 or self.edgesList.currentItem() == None:
            return
        selected = self.edgesList.currentItem()
        self.graph.remove_edges_from([(selected.text()[1], selected.text()[3])])
        self.updateGraph()


    def clearEdges(self):
        self.graph.clear_edges()
        self.updateGraph()

    def checkConnection(self):
        g = Graph(list(self.graph.edges),self.graph.nodes)
        if isGraphStronglyConnected(g):
            text = "Graf jest silnie spójny"
        else:
            text = "Graf nie jest silnie spójny"
        plt.title(text,fontsize=20)
        pos = nx.circular_layout(self.graph, scale=2)
        nx.draw(self.graph, pos, node_color='orange', with_labels=True, arrows=True, arrowsize=15, edgecolors='black')
        fig = plt.gcf()
        fig.canvas.set_window_title(f'{text}')
        plt.show()

    def toggleInfo(self):
        if self.infoWidget.isHidden():
            self.infoWidget.show()
        else:
            self.infoWidget.hide()

    def updateGraph(self):
        self.setupUi(self.MainWindow)

        for node in list(self.graph.nodes):
            item = QListWidgetItem(node)
            item.setSizeHint(QSize(250,20))
            item.setTextAlignment(Qt.AlignHCenter)
            self.nodesList.addItem(item)

        for edge in list(self.graph.edges):
            edge = QListWidgetItem(f'({edge[0]},{edge[1]})')
            edge.setTextAlignment(Qt.AlignHCenter)
            self.edgesList.addItem(edge)
        self.infoWidget.hide()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())