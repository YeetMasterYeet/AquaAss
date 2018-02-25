#!/usr/bin/python3

import sys
import dialogs
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(280,40)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Somebody clicka da button')
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message', "You typed " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
