# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgetresults.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class ResultsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Results")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.setFont(font)

        # displaying the widgets in a grid

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.title = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")

        self.graphicsView = QtWidgets.QLabel(self)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)


        self.graphicsView_2 = QtWidgets.QLabel(self)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.graphicsView_2, 1, 1, 1, 1)

        self.graphicsView_3 = QtWidgets.QLabel(self)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.graphicsView_3, 1, 2, 1, 1)


        self.day1 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.day1.setFont(font)
        self.day1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.day1.setObjectName("label")
        self.gridLayout.addWidget(self.day1, 2, 0, 1, 1)

        self.day3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.day3.setFont(font)
        self.day3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.day3.setObjectName("day3")
        self.gridLayout.addWidget(self.day3, 2, 2, 1, 1)

        self.weathertype1 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.weathertype1.setFont(font)
        self.weathertype1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weathertype1.setObjectName("weathertype1")
        self.gridLayout.addWidget(self.weathertype1, 3, 0, 1, 1)

        self.day2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.day2.setFont(font)
        self.day2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.day2.setObjectName("day2")
        self.gridLayout.addWidget(self.day2, 2, 1, 1, 1)

        self.maxt1 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.maxt1.setFont(font)
        self.maxt1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.maxt1.setObjectName("maxt1")
        self.gridLayout.addWidget(self.maxt1, 4, 0, 1, 1)

        self.weathertype2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.weathertype2.setFont(font)
        self.weathertype2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weathertype2.setObjectName("weathertype2")
        self.gridLayout.addWidget(self.weathertype2, 3, 1, 1, 1)

        self.weathertype3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.weathertype3.setFont(font)
        self.weathertype3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weathertype3.setObjectName("weathertype3")
        self.gridLayout.addWidget(self.weathertype3, 3, 2, 1, 1)

        self.maxt2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.maxt2.setFont(font)
        self.maxt2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.maxt2.setObjectName("maxt2")
        self.gridLayout.addWidget(self.maxt2, 4, 1, 1, 1)

        self.maxt3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.maxt3.setFont(font)
        self.maxt3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.maxt3.setObjectName("maxt3")
        self.gridLayout.addWidget(self.maxt3, 4, 2, 1, 1)

        self.mint = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.mint.setFont(font)
        self.mint.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mint.setObjectName("mint")
        self.gridLayout.addWidget(self.mint, 5, 0, 1, 1)

        self.mint2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.mint2.setFont(font)
        self.mint2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mint2.setObjectName("mint2")
        self.gridLayout.addWidget(self.mint2, 5, 1, 1, 1)

        self.mint3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.mint3.setFont(font)
        self.mint3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mint3.setObjectName("mint3")
        self.gridLayout.addWidget(self.mint3, 5, 2, 1, 1)

        # adding spacing above the button
        self.spacer = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacer, 6, 0, 1, 3)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.backButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.backButton.setText("Back")
        self.gridLayout.addWidget(self.backButton, 7, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        # adding spacing below button
        self.gridLayout.addItem(self.spacer, 8, 0, 1, 3)

        QtCore.QMetaObject.connectSlotsByName(self)

