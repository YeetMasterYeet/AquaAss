#!/usr/bin/python3

import sys

from pathlib import Path
from FMTKDialog       import *
from TestStripsDialog import *
from UpdateTempDialog import *
from PyQt5.QtWidgets  import *
from PyQt5.QtCore     import *
from PyQt5.QtGui      import *

class AquaAss(QWidget):

    # store previous temp
    prev_temp      = "n/a";
    # store previous test strip test values
    ts_prev_GH     = "n/a";
    ts_prev_KH     = "n/a";
    ts_prev_pH     = "n/a";
    ts_prev_NO2    = "n/a";
    ts_prev_NO3    = "n/a";
    # store previous fmtk test values
    fmtk_prev_pH   = "n/a";
    fmtk_prev_HRpH = "n/a";
    fmtk_prev_Amm  = "n/a";
    fmtk_prev_NO2  = "n/a";
    fmtk_prev_NO3  = "n/a";

    tsGroup = None
    fmtkGroup = None
    tempGroup = None

    def __init__(self):
        super(AquaAss, self).__init__()

        self.title  = 'Aquarium Assistant v0.0.1'
        self.left   = 10
        self.top    = 10
        self.width  = 400
        self.height = 300
        self.drawMain()

    def drawMain(self):
        self.readPreviousValues()

        self.tsGroup   = self.createTSGroup()
        self.fmtkGroup = self.createFMTKGroup()
        self.tempGroup = self.createTempGroup()
 
        grid = QGridLayout()
        grid.addWidget(self.tsGroup, 0, 0)
        grid.addWidget(self.fmtkGroup, 0, 1)
        grid.addWidget(self.tempGroup, 1, 0)
        self.setLayout(grid)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def readPreviousValues(self):
        file = Path(".aquadata")
        if file.is_file():
            with open(".aquadata", "r") as fp:
                fmtkLine = fp.readline()
                tsLine   = fp.readline()
                tempLine = fp.readline()
    
                self.ts_prev_GH  = tsLine.split(',')[0];
                self.ts_prev_KH  = tsLine.split(',')[1];
                self.ts_prev_pH  = tsLine.split(',')[2];
                self.ts_prev_NO2 = tsLine.split(',')[3];
                self.ts_prev_NO3 = tsLine.split(',')[4];
                
                self.fmtk_prev_pH    = fmtkLine.split(',')[0];
                self.fmtk_prev_HRpH  = fmtkLine.split(',')[1];
                self.fmtk_prev_Amm   = fmtkLine.split(',')[2];
                self.fmtk_prev_NO2   = fmtkLine.split(',')[3];
                self.fmtk_prev_NO3   = fmtkLine.split(',')[4];
                
                self.prev_temp = tempLine
        else:
            with open(".aquadata", "w") as fp:
                fp.write("'n/a','n/a','n/a','n/a','n/a'\n")
                fp.write("'n/a','n/a','n/a','n/a','n/a'\n")
                fp.write("'n/a'\n")


    def createTSGroup(self):
        tsGroupBox = QGroupBox("5-in-1 Test Strips")

        prevTestLabel = QLabel('Previous Test Results:')
        prevTestLabel.setStyleSheet("font-style:italic")
        prevTestLabelGH = QLabel('    GH Level: \t' + self.ts_prev_GH)
        prevTestLabelGH.setStyleSheet("font-style:italic")
        prevTestLabelKH = QLabel('    KH Level: \t' + self.ts_prev_KH)
        prevTestLabelKH.setStyleSheet("font-style:italic")
        prevTestLabelpH = QLabel('    pH Level: \t' + self.ts_prev_pH)
        prevTestLabelpH.setStyleSheet("font-style:italic")
        prevTestLabelNO2 = QLabel('    Nitrite Level: \t' + self.ts_prev_NO2)
        prevTestLabelNO2.setStyleSheet("font-style:italic")
        prevTestLabelNO3 = QLabel('    Nitrate Level: \t' + self.ts_prev_NO3) 
        prevTestLabelNO3.setStyleSheet("font-style:italic")

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

        prevTestLabel     = QLabel("Previous Test Results:")
        prevTestLabel.setStyleSheet("font-style:italic")
        prevTestLabelpH   = QLabel('    pH Level: \t\t' + self.fmtk_prev_pH)
        prevTestLabelpH.setStyleSheet("font-style:italic")
        prevTestLabelHRpH = QLabel('    HRpH Level: \t\t' + self.fmtk_prev_HRpH)
        prevTestLabelHRpH.setStyleSheet("font-style:italic")
        prevTestLabelAmm  = QLabel('    Ammonia Level: \t' + self.fmtk_prev_Amm)
        prevTestLabelAmm.setStyleSheet("font-style:italic")
        prevTestLabelNO2  = QLabel('    Nitrite Level: \t\t' + self.fmtk_prev_NO2)
        prevTestLabelNO2.setStyleSheet("font-style:italic")
        prevTestLabelNO3  = QLabel('    Nitrate Level: \t\t' + self.fmtk_prev_NO3)
        prevTestLabelNO3.setStyleSheet("font-style:italic")

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

        prevTempLabel = QLabel("Previous Reading: " + self.prev_temp)
        prevTempLabel.setStyleSheet("font-style:italic")

        updateTempButton = QPushButton('Update')
        updateTempButton.setToolTip('Update the temperature of the water in the aquarium')
        updateTempButton.setFixedWidth(120)
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
        self.close()
        tsDialog.exec_()
        self.__init__()

    @pyqtSlot()
    def FMTK_click(self):
        fmtkDialog = FMTKDialog()
        self.close()
        fmtkDialog.exec_()
        self.__init__()

    @pyqtSlot()
    def updateTemp_click(self):
        utDialog = UpdateTempDialog()
        self.close()
        utDialog.exec_()
        self.__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AquaAss()
    sys.exit(app.exec_())
