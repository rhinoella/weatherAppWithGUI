from datetime import date
from PyQt5 import QtWidgets
from mainwindowUI import MainWindow
from weatherModel import WeatherModel
import sys


class CityWeather:
   def __init__(self, model, view):
      print("created cityweather")
      self._model = model
      self._view = view
      self.getinput()

      self.city = "Placeholder"
      self.geocoding = None
      self.latitude = "latitude"
      self.longitude = "longitude"
      self.weather = "weather"
      self.maxTemp = 0
      self.minTemp = 0

      # the description of the data from the API
      self.weatherCodes = {
         "ishower": "Slightly cloudy with light precipitation",
         "clear": "Clear",
         "pcloudy": "Slightly cloudy",
         "mcloudy": "Cloudy",
         "cloudy": "Cloudy",
         "humid": "Humid",
         "lightrain": "Cloudy with light precipitation",
         "oshower": "Cloudy with light precipitation",
         "lightsnow": "Light snow",
         "rain": "Rainy",
         "snow": "Snowy",
         "rainsnow": "Cold rain with a chance of hail",
         "ts": "Thunderstorm with slight rain",
         "tsrain": "Thunderstorm with heavy rain"
      }


   def getinput(self):
      print("connected buttonpress to func")
      self._view.lineEdit.returnPressed.connect(self.submit)
      self._view.pushButton.clicked.connect(self.submit)

   def submit(self):
      print("button has been pressed")
      validInput = self._model.inputcheck(input=self._view.gettext(), cityWeather=self)
      if not validInput:
         self._view.inputfailed()
         self._view.lineEdit.clear()
      else:
         self._model.getgeocode(self)
         self._model.getweather(self)


def main():
   app = QtWidgets.QApplication(sys.argv)
   Dialog = QtWidgets.QDialog()
   weatherUi = MainWindow(Dialog)
   Dialog.show()
   weatherModel = WeatherModel()
   CityWeather(model = weatherModel, view = weatherUi)
   sys.exit(app.exec_())


if __name__ == "__main__":
    main()