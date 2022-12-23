from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType



ui,_ = loadUiType('insertion.ui')

class Sort(QWidget , ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Insertion Sort")
        self.Handel_Buttons()


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.ascending)
        self.pushButton_2.clicked.connect(self.descending)

    def ascending(self):
        arr = self.lineEdit.text().split()
        arr = [int(x) for x in arr]
        sorted = self.insertionSort(arr)
        self.lineEdit_2.setText(str(sorted))

    def descending(self):
        arr = self.lineEdit.text().split()
        arr = [int(x) for x in arr]
        sorted = self.insertionSort(arr)
        sorted.reverse()
        self.lineEdit_2.setText(str(sorted))

    def insertionSort(self,arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


def main():
    app = QApplication(sys.argv)
    window = Sort()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()