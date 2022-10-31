import requests
import datetime
import os
from PyQt5 import QtGui, QtCore


# the model stores the data and does the logic
class WeatherModel(object):
    def __init__(self):

        #the data for the weather
        print("created weathermodel")
        self._city = "Placeholder"
        self._geocoding = None
        self._latitude = "latitude"
        self._longitude = "longitude"
        self._weather = ["d1","d2", "d3"]
        self._maxTemp = ["d1","d2", "d3"]
        self._minTemp = ["d1","d2", "d3"]
        self._weatherRaw = ["d1","d2", "d3"]

        #gets the name of the days (today, tommorow and the day after tommorow)
        now = datetime.datetime.now()
        tommorow = now + datetime.timedelta(days=1)
        dayatommorow = now + datetime.timedelta(days=2)
        self._d1 = now.strftime("%A")
        self._d2 = tommorow.strftime("%A")
        self._d3 = dayatommorow.strftime("%A")

        #to convert the weather codes from the API to a readable description
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

    #getter functions
    @property
    def city(self):
        return self._city

    @property
    def weather(self):
        return self._weather

    @property
    def rawWeather(self):
        return self._weatherRaw

    @property
    def maxTemp(self):
        return self._maxTemp

    @property
    def minTemp(self):
        return self._minTemp

    @property
    def d1(self):
        return self._d1

    @property
    def d2(self):
        return self._d2

    @property
    def d3(self):
        return self._d3

    # check the input to see if it is valid
    def inputcheck(self, input):
        print("input checking in progress...")
        try:
            int(input) # if the input is an int (the API takes int parameters, but we don't want it in int form)
        except: # if it is a string (what we want)
            # this will acess the API that converts city names to their geocode
            geocoding = requests.get(f"https://nominatim.openstreetmap.org/search?city={input}&format=json")
            if len(geocoding.json()) == 0:  # if the city doesn't exist, the json file will be empty
                return False
            else:
                self._geocoding = geocoding
                self._city = input.capitalize()
                return True
        else:  # if it is an int, function will return false
            return False

    # sets the longitude and latitude of to city -> the weather API only takes geocodes
    def getgeocode(self):
        # the data is a dictionary within a list so the list must be accessed first
        dataList = self._geocoding.json()[0]
        self._latitude = dataList["lat"]
        self._longitude = dataList["lon"]
        print(f"{self._longitude}, {self._latitude}\n\n")

    def getweather(self):
        weather = requests.get(
            f"https://7timer.info/bin/api.pl?lon={self._longitude}&lat={self._latitude}&product=civillight&output=json")
        weekData = weather.json()["dataseries"]  # the data is dictionaries within a list within a dictionary
        d1 = weekData[0]
        d2 = weekData[1]
        d3 = weekData[2]

        # 'raw' weather is the weather codes given by the API
        self._weatherRaw = [d1["weather"], d2["weather"], d3["weather"]]

        # gets the weather in an english description
        self._weather = [self.weatherCodes[self._weatherRaw[0]], self.weatherCodes[self._weatherRaw[1]], self.weatherCodes[self._weatherRaw[2]]]
        self._maxTemp = [d1["temp2m"]["max"], d2["temp2m"]["max"], d3["temp2m"]["max"]]
        self._minTemp = [d1["temp2m"]["min"], d2["temp2m"]["min"], d3["temp2m"]["min"]]
        print("got weather")
        print(self._maxTemp)
        print(self._weather)

    def getIcon(self):  # will get the icon for the weather type
        imageProfile = []
        # To scale image for example and keep its Aspect Ratio
        dirPath = os.path.join(os.path.dirname(__file__), r'weatherIcons')

        for i in range(3):
            imgPath = os.path.join(dirPath, f'{self._weatherRaw[i]}.png')
            imageProfile.append(QtGui.QImage(imgPath))
            print(imgPath)
            imageProfile[i] = imageProfile[i].scaled(200, 200, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                          transformMode=QtCore.Qt.TransformationMode.SmoothTransformation)

        return imageProfile