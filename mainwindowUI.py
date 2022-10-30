from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, _inputWidget, _resultsWidget):
        super().__init__()

        self.inputWidget = _inputWidget
        self.resultsWidget = _resultsWidget

        # creating stacked widgets, so we can switch inbetween the input and result screens
        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.inputWidget)
        self.stack.addWidget(self.resultsWidget)
        self.stack.setCurrentWidget(self.inputWidget)

        window = QtWidgets.QWidget()
        mainLayout = QHBoxLayout()

        window.setLayout(mainLayout)
        mainLayout.addWidget(self.stack)

        self.setCentralWidget(window)
        self.resize(1000, 450)
        self.setMinimumSize(QtCore.QSize(800, 350)) # sets the size of the window
        self.setWindowTitle("Noella's Weather App")

        QtCore.QMetaObject.connectSlotsByName(self)

    def editresults(self, imageProfile, model):
        # to edit the results screen
        print("results being edited...")

        self.resultsWidget.title.setText(model.city)
        self.setWindowTitle(f"{model.city} Weather")

        self.resultsWidget.graphicsView.setPixmap(QtGui.QPixmap.fromImage(imageProfile[0]))
        self.resultsWidget.graphicsView_2.setPixmap(QtGui.QPixmap.fromImage(imageProfile[1]))
        self.resultsWidget.graphicsView_3.setPixmap(QtGui.QPixmap.fromImage(imageProfile[2]))

        self.resultsWidget.day1.setText(model.d1)
        self.resultsWidget.day2.setText(model.d2)
        self.resultsWidget.day3.setText(model.d3)

        self.resultsWidget.weathertype1.setText(model.weather[0])
        self.resultsWidget.weathertype2.setText(model.weather[1])
        self.resultsWidget.weathertype3.setText(model.weather[2])

        self.resultsWidget.maxt1.setText(f"{model.maxTemp[0]}")
        self.resultsWidget.maxt2.setText(f"{model.maxTemp[1]}")
        self.resultsWidget.maxt3.setText(f"{model.maxTemp[2]}")

        self.resultsWidget.mint.setText(f"{model.minTemp[0]}")
        self.resultsWidget.mint2.setText(f"{model.minTemp[1]}")
        self.resultsWidget.mint3.setText(f"{model.minTemp[2]}")

        self.stack.setCurrentWidget(self.resultsWidget)



