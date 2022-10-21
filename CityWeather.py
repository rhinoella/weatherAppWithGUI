import requests


# class to contain all the information about the city
class CityWeather:
   city = "city"
   latitude = "latitude"
   longitude = "longitude"
   weather = "weather"
   maxTemp = 0
   minTemp = 0

   # the description of the data from the API
   weatherCodes = {
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

   # will get the user input for the desired city and access the API to get and return the JSON file
   def getinput(self):
      inputCheck = False
      while not inputCheck:
         city = input("Welcome to noella's weather app!\nPlease type the city you want to recieve the weather for :\n\n")

         try:
            int(city)
         except:
            geocoding = requests.get(f"https://nominatim.openstreetmap.org/search?city={city}&format=json")
            if len(geocoding.json()) == 0:
               print("City does not exist, try again.\n")
            else:
               inputCheck = True
               self.city = city  # sets the city name
               return geocoding
         else:
            print("Invalid input, try again\n")


   # sets the longitude and latitude within the city object
   def getgeocode(self, geocoding):
      dataList = geocoding.json()[0]  # the data is a dictionary within a list so the list must be accessed first
      latitude = dataList["lat"]
      longitude = dataList["lon"]
      self.latitude = latitude
      self.longitude = longitude
      print(f"{longitude}, {latitude}\n\n")


   def getweather(self):
      weather = requests.get(f"https://7timer.info/bin/api.pl?lon={self.longitude}&lat={self.latitude}&product=civillight&output=json")
      weekData = weather.json()["dataseries"]  # the data is dictionaries within a list within a dictionary
      todayData = weekData[0]
      self.weather = todayData["weather"]
      self.maxTemp = todayData["temp2m"]["max"]
      self.minTemp = todayData["temp2m"]["min"]