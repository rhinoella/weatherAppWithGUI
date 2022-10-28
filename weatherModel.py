import requests

class WeatherModel:

   def inputcheck(self, input, cityWeather):
      # check the input
      print("Clicked")
      try:
         int(input)
      except:
         geocoding = requests.get(f"https://nominatim.openstreetmap.org/search?city={input}&format=json")
         if len(geocoding.json()) == 0:
            return False
         else:
            cityWeather.geocoding = geocoding
            cityWeather.city = input
            return True
      else:
         return False

   # sets the longitude and latitude within the city object
   def getgeocode(self, cityWeather):
      dataList = cityWeather.geocoding.json()[0]  # the data is a dictionary within a list so the list must be accessed first
      latitude = dataList["lat"]
      longitude = dataList["lon"]
      cityWeather.latitude = latitude
      cityWeather.longitude = longitude
      print(f"{longitude}, {latitude}\n\n")


   def getweather(cityWeather):
      weather = requests.get(f"https://7timer.info/bin/api.pl?lon={cityWeather.longitude}&lat={cityWeather.latitude}&product=civillight&output=json")
      weekData = weather.json()["dataseries"]  # the data is dictionaries within a list within a dictionary
      todayData = weekData[0]
      cityWeather.weather = todayData["weather"]
      cityWeather.maxTemp = todayData["temp2m"]["max"]
      cityWeather.minTemp = todayData["temp2m"]["min"]