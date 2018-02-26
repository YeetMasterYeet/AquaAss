#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
import datetime

class UpdateTempDialog(QDialog):
    WaterTempBox = None
 
    def __init__(self):
        super(UpdateTempDialog, self).__init__()

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
        self.formGroupBox = QGroupBox("Update Water Temperature")
        layout = QFormLayout()

        layout.addRow(QLabel("Current Water Temperature (F):"), self.WaterTempBox)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        date = datetime.datetime.now()
        print("\nWater Temperature - " + str(date))

        temperature = self.WaterTempBox.text()
        print("  Temperature (F):\t\t" + temperature) 

        self.writeTemperature(temperature)

        self.done(0)

    def writeTemperature(self, temp):
        with open(".aquadata", "r") as fp:
            tsLine   = fp.readline()
            fmtkLine = fp.readline()
            tempLine = fp.readline()

        with open(".aquadata", "w") as fp:
            fp.write(tsLine)
            fp.write(fmtkLine)
            fp.write(temp)
            fp.write("\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UpdateTempDialog()
    sys.exit(dialog.exec_())
