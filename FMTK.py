#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
import datetime

class FMTKDialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
    phBox = None
    HRphBox = None
    AmmBox = None
    NO2Box = None
    NO3Box = None
 
    def __init__(self):
        super(FMTKDialog, self).__init__()

        self.phBox = QComboBox()
        self.HRphBox = QComboBox()
        self.AmmBox = QComboBox()
        self.NO2Box = QComboBox()
        self.NO3Box = QComboBox()

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
        self.formGroupBox = QGroupBox("Freshwater Master Test Kit")
        layout = QFormLayout()

        # Create the pH combobox
        phItems = ['6.0','6.4','6.6','7.0','7.2','7.6+']
        self.phBox.addItems(phItems)

        # Create the HRpH combobox
        HRphItems = ['N/A','7.4','7.8','8.0','8.2','8.4','8.8']
        self.HRphBox.addItems(HRphItems)

        # Create the Ammonia combobox
        AmmItems = ['0 ppm','0.25 ppm','0.50 ppm','1.0 ppm','2.0 ppm','4.0 ppm','8.0 ppm']
        self.AmmBox.addItems(AmmItems)

        # Create the Nitrite combobox
        NO2Items = ['0 ppm','0.25 ppm','0.50 ppm','1.0 ppm','2.0 ppm','5.0 ppm']
        self.NO2Box.addItems(NO2Items)

        # Create the Nitrate combobox
        NO3Items = ['0 ppm','5 ppm','10 ppm','20 ppm','40 ppm','80 ppm','100 ppm']
        self.NO3Box.addItems(NO3Items)

        layout.addRow(QLabel("pH:"), self.phBox)
        layout.addRow(QLabel("High Range pH:"), self.HRphBox)
        layout.addRow(QLabel("Ammonia (NH3/NH4+):"), self.AmmBox)
        layout.addRow(QLabel("Nitrite (NO2-):"), self.NO2Box)
        layout.addRow(QLabel("Nitrate (NO3-):"), self.NO3Box)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        date = datetime.datetime.now()
        print("\nFreshwater Master Test Kit Results - " + str(date))
        print("  pH Level:\t\t" + self.phBox.currentText()) 
        print("  High Range pH Level:\t" + self.HRphBox.currentText()) 
        print("  Ammonia Level:\t" + self.AmmBox.currentText()) 
        print("  Nitrite Level:\t" + self.NO2Box.currentText()) 
        print("  Nitrate Level:\t" + self.NO3Box.currentText()) 
        self.done(0)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = FMTKDialog()
sys.exit(dialog.exec_())
