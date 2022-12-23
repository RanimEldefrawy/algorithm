from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType



ui,_ = loadUiType('merge.ui')

class Merge(QWidget , ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Merge Sort")
        self.Handel_Buttons()


    def Handel_Buttons(self):

        self.pushButton.clicked.connect(self.ascending)
        self.pushButton_2.clicked.connect(self.descending)

    def ascending(self):
        arr = self.lineEdit.text().split()
        arr = [int(x) for x in arr]
        sorted=self.mergeSort(arr)
        self.lineEdit_2.setText(str(sorted))

    def descending(self):
        arr = self.lineEdit.text().split()
        arr = [int(x) for x in arr]
        sorted = self.mergeSort(arr)
        sorted.reverse()
        self.lineEdit_2.setText(str(sorted))

    def mergeSort(self,arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr



def main():
    app = QApplication(sys.argv)
    window = Merge()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()