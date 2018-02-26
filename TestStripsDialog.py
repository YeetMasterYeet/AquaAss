#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
import datetime

class TestStripsDialog(QDialog):
    GHBox = None
    KHBox = None
    pHBox = None
    NO2Box = None
    NO3Box = None
 
    def __init__(self):
        super(TestStripsDialog, self).__init__()

        self.GHBox = QComboBox()
        self.KHBox = QComboBox()
        self.pHBox = QComboBox()
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
        self.formGroupBox = QGroupBox("5-in-1 Test Strips")
        layout = QFormLayout()

        # Create the GH combobox
        GHItems = ['0','30','60','120','180']
        self.GHBox.addItems(GHItems)

        # Create the KH combobox
        KHItems = ['0','40','80','120','180','240']
        self.KHBox.addItems(KHItems)

        # Create the pH combobox
        pHItems = ['6.0','6.5','7.0','7.5','8.0','8.5','9.0']
        self.pHBox.addItems(pHItems)

        # Create the Nitrite combobox
        NO2Items = ['0 ppm','0.50 ppm','1.0 ppm','3.0 ppm','5.0 ppm','10.0 ppm']
        self.NO2Box.addItems(NO2Items)

        # Create the Nitrate combobox
        NO3Items = ['20 ppm','40 ppm','80 ppm','160 ppm','200 ppm']
        self.NO3Box.addItems(NO3Items)

        layout.addRow(QLabel("General Hardness (GH):"), self.GHBox)
        layout.addRow(QLabel("Carbonate Hardness (KH):"), self.KHBox)
        layout.addRow(QLabel("pH"), self.pHBox)
        layout.addRow(QLabel("Nitrite (NO2-):"), self.NO2Box)
        layout.addRow(QLabel("Nitrate (NO3-):"), self.NO3Box)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        date = datetime.datetime.now()
        print("\n5-in-1 Test Strip Results - " + str(date))
        print("  GH Level:\t\t" + self.GHBox.currentText()) 
        print("  KH Level:\t\t" + self.KHBox.currentText()) 
        print("  pH Level:\t\t" + self.pHBox.currentText()) 
        print("  Nitrite Level:\t" + self.NO2Box.currentText()) 
        print("  Nitrate Level:\t" + self.NO3Box.currentText()) 

        self.writeTestStrips(self.GHBox.currentText(), self.KHBox.currentText(), self.pHBox.currentText(), self.NO2Box.currentText(), self.NO3Box.currentText())

        self.done(0)

    def writeTestStrips(self, GH, KH, pH, NO2, NO3):
        with open(".aquadata", "r") as fp:
            tsLine   = fp.readline()
            fmtkLine = fp.readline()
            tempLine = fp.readline()

        fmtkLine = GH + "," + KH + "," + pH + "," + NO2 + "," + NO3 + "\n"

        with open(".aquadata", "w") as fp:
            fp.write(tsLine)
            fp.write(fmtkLine)
            fp.write(tempLine)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = TestStripsDialog()
    sys.exit(dialog.exec_())
