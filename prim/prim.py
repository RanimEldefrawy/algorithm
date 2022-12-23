from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import numpy as np


ui,_ = loadUiType('prim.ui')

class Prim(QWidget , ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Prim's Algorithm")
        self.Handel_Buttons()

    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.MST)

    def MST(self):

        INF = 9999999
        Vertex =int(self.lineEdit.text())
        r=int(self.lineEdit_2.text())
        c=int(self.lineEdit_3.text())
        G=self.lineEdit_4.text().split()
        G=[int(x) for x in G]
        Graph = np.array(G).reshape(r, c)

        selected = [0, 0, 0, 0, 0]
        no_edge = 0
        selected[0] = True
        while (no_edge < Vertex - 1):
            minimum = INF
            x = 0
            y = 0
            for i in range(Vertex):
                if selected[i]:
                    for j in range(Vertex):
                        if ((not selected[j]) and Graph[i][j]):
                            if minimum > Graph[i][j]:
                                minimum = Graph[i][j]
                                x = i
                                y = j
            self.textEdit.append(str(x) + " - " + str(y) + " : " + str(Graph[x][y]) )
            selected[y] = True
            no_edge += 1


def main():
    app = QApplication(sys.argv)
    window = Prim()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

#Used in testing
#vertex=5 , rows =5 , columns=5
# 0 9 75 0 0 9 0 95 19 42 75 95 0 51 66 0 19 51 0 31 0 42 66 31 0