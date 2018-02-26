#!/usr/bin/python3

import sys
from FMTKDialog import *
from TestStripsDialog import *
from UpdateTempDialog import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class AquaAss(QWidget):
    prev_temp = "n/a";

    ts_prev_GH = "n/a";
    ts_prev_KH = "n/a";
    ts_prev_pH = "n/a";
    ts_prev_NO2 = "n/a";
    ts_prev_NO3 = "n/a";

    fmtk_prev_pH = "n/a";
    fmtk_prev_HRpH = "n/a";
    fmtk_prev_Amm = "n/a";
    fmtk_prev_NO2 = "n/a";
    fmtk_prev_NO3 = "n/a";

    def __init__(self, parent=None):
        super(AquaAss, self).__init__(parent)

        self.title = 'Aquarium Assistant v0.0.1'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300

        grid = QGridLayout()
        grid.addWidget(self.createTSGroup(), 0, 0)
        grid.addWidget(self.createFMTKGroup(), 0, 1)
        grid.addWidget(self.createTempGroup(), 1, 0)
        self.setLayout(grid)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def createTSGroup(self):
        tsGroupBox = QGroupBox("5-in-1 Test Strips")

        prevTestLabel = QLabel('Previous Test Results:')
        prevTestLabel.setStyleSheet("font-style:italic")
        prevTestLabelGH = QLabel('    GH Level: \t' + self.ts_prev_GH)
        prevTestLabelKH = QLabel('    KH Level: \t' + self.ts_prev_KH)
        prevTestLabelpH = QLabel('    pH Level: \t' + self.ts_prev_pH)
        prevTestLabelNO2 = QLabel('    Nitrite Level: \t' + self.ts_prev_NO2)
        prevTestLabelNO3 = QLabel('    Nitrate Level: \t' + self.ts_prev_NO3) 

        testStripsButton = QPushButton('Run 5-in-1 Test')
        testStripsButton.setToolTip('Import the results from a test strip testing.')
        testStripsButton.setFixedWidth(120)
        testStripsButton.clicked.connect(self.testStrips_click)

        # Test strip layout
        tsLayout = QVBoxLayout()
        tsLayout.addWidget(prevTestLabel)
        tsLayout.addWidget(prevTestLabelGH)
        tsLayout.addWidget(prevTestLabelKH)
        tsLayout.addWidget(prevTestLabelpH)
        tsLayout.addWidget(prevTestLabelNO2)
        tsLayout.addWidget(prevTestLabelNO3)
        tsLayout.addWidget(testStripsButton)
        tsLayout.addStretch(1)
        tsGroupBox.setLayout(tsLayout)

        return tsGroupBox

    def createFMTKGroup(self):
        FMTKGroupBox = QGroupBox("Freshwater Master Test Kit")

        prevTestLabel = QLabel("Previous Test Results:")
        prevTestLabel.setStyleSheet("font-style:italic")
        prevTestLabelpH = QLabel('pH Level: \t' + self.fmtk_prev_pH)
        prevTestLabelHRpH = QLabel('HRpH Level: \t' + self.fmtk_prev_HRpH)
        prevTestLabelAmm = QLabel('Ammonia Level: \t' + self.fmtk_prev_Amm)
        prevTestLabelNO2 = QLabel('Nitrite Level: \t' + self.fmtk_prev_NO2)
        prevTestLabelNO3 = QLabel('Nitrate Level: \t' + self.fmtk_prev_NO3)

        FMTKButton = QPushButton('Run FMTK Test')
        FMTKButton.setToolTip('Import the results from a master tesk kit testing.')
        FMTKButton.setFixedWidth(120)
        FMTKButton.clicked.connect(self.FMTK_click)

        # Test strip layout
        layout = QVBoxLayout()
        layout.addWidget(prevTestLabel)
        layout.addWidget(prevTestLabelpH)
        layout.addWidget(prevTestLabelHRpH)
        layout.addWidget(prevTestLabelAmm)
        layout.addWidget(prevTestLabelNO2)
        layout.addWidget(prevTestLabelNO3)
        layout.addWidget(FMTKButton)
        layout.addStretch(1)
        FMTKGroupBox.setLayout(layout)

        return FMTKGroupBox

    def createTempGroup(self):
        tempGroupBox = QGroupBox("Water Temperature")

        prevTempLabel = QLabel("Most Recent Temperature Reading: " + self.prev_temp)
        prevTempLabel.setStyleSheet("font-style:italic")

        updateTempButton = QPushButton('Update Water Temperature')
        updateTempButton.setToolTip('Update the temperature of the water in the aquarium')
        updateTempButton.setFixedWidth(200)
        updateTempButton.clicked.connect(self.updateTemp_click)

        layout = QVBoxLayout()
        layout.addWidget(prevTempLabel)
        layout.addWidget(updateTempButton)
        layout.addStretch(1)
        tempGroupBox.setLayout(layout)

        return tempGroupBox

    @pyqtSlot()
    def testStrips_click(self):
        tsDialog = TestStripsDialog()
        tsDialog.exec_()

    @pyqtSlot()
    def FMTK_click(self):
        fmtkDialog = FMTKDialog()
        fmtkDialog.exec_()

    @pyqtSlot()
    def updateTemp_click(self):
        utDialog = UpdateTempDialog()
        utDialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AquaAss()
    sys.exit(app.exec_())
