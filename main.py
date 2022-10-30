from PyQt5 import QtWidgets
import sys
from widgetinput import InputWidget
from mainwindowUI import MainWindow
from weatherController import WeatherController
from weatherModel import WeatherModel
from widgetresults import ResultsWidget


def main():
    app = QtWidgets.QApplication(sys.argv) # creating the app
    # creating the widget objects - must do this in main otherwise the objects are deleted
    inputWidget = InputWidget()
    resultsWidget = ResultsWidget()
    weatherModel = WeatherModel()
    weatherUi = MainWindow(inputWidget, resultsWidget)
    weatherUi.show()
    controller = WeatherController(view=weatherUi, model=weatherModel)  # must create a persistent object, otherwise it gets deleted
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
