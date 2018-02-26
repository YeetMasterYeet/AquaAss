#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
import datetime

class UpdateTempDialog(QDialog):
    NumGridRows = 1
    NumButtons = 4
    WaterTempBox = None
 
    def __init__(self):
        super(UpdateTempDialog, self).__init__()
        print("Initializing UpdateTempDialog")

        self.WaterTempBox = QLineEdit()

        self.createFormGroupBox()
 
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
 
        self.setWindowTitle("Aquarium Data Form")
 
    def createFormGroupBox(self):
        print("Creating Form GroupBox")

        self.formGroupBox = QGroupBox("Update Water Temperature")
        layout = QFormLayout()

        layout.addRow(QLabel("Current Water Temperature (F):"), self.WaterTempBox)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        date = datetime.datetime.now()
        print("\nWater Temperature - " + str(date))
        print("  Temperature (F):\t\t" + self.WaterTempBox.text()) 
        self.done(0)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UpdateTempDialog()
    sys.exit(dialog.exec_())
