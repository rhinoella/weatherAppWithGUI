import requests
from datetime import date


class CityWeather:
   city = "city"
   latitude = "latitude"
   longitude = "longitude"
   weather = "weather"
   maxTemp = 0
   minTemp = 0


# the description of the data from the API
weatherCodes = {
   "ishower" : "Slightly cloudy with light precipitation",
   "clear" : "Clear",
   "pcloudy" : "Slightly cloudy",
   "mcloudy" : "Cloudy",
   "cloudy" : "Cloudy",
   "humid" : "Humid",
   "lightrain" : "Cloudy with light precipitation",
   "oshower" : "Cloudy with light precipitation",
   "lightsnow" : "Light snow",
   "rain" : "Rainy",
   "snow" : "Snowy",
   "rainsnow" : "Cold rain with a chance of hail",
   "ts" : "Thunderstorm with slight rain",
   "tsrain" : "Thunderstorm with heavy rain"
}

# uses datetime to get the date
def getdate():
   dateToday = date.today()
   return dateToday


# will get the user input for the desired city and access the API to get and return the JSON file
def getinput(cityObj):
   inputCheck = False
   while not inputCheck:
       city = input("welcome to noella's weather app!\nplease type the city you want to recieve the weather for :\n\n")

       if isinstance(city, str):  # if the input is a string
           try:
               geocoding = requests.get(f"https://nominatim.openstreetmap.org/search?city={city}&format=json")
           except:   # if the city is invalid this exception will occur
               print("city does not exist")
       inputCheck = True
       cityObj.city = city   # sets the city name
   return geocoding


# sets the longitude and latitude within the city object
def getgeocode(geocoding, cityObj):
   dataList = geocoding.json()[0]  # the data is a dictionary within a list so the list must be accessed first
   latitude = dataList["lat"]
   longitude = dataList["lon"]
   cityObj.latitude = latitude
   cityObj.longitude = longitude
   print(f"{longitude}, {latitude}\n\n")


def main():
   newCity = CityWeather
   geocoding = getinput(newCity)
   getgeocode(geocoding, newCity)
   weather = requests.get(
       f"https://7timer.info/bin/api.pl?lon={newCity.longitude}&lat={newCity.latitude}&product=civillight&output=json")
   weekData = weather.json()["dataseries"] # the data is dictionaries within a list within a dictionary
   todayData = weekData[0]
   newCity.weather = todayData["weather"]
   newCity.maxTemp = todayData["temp2m"]["max"]
   newCity.minTemp = todayData["temp2m"]["min"]

   print(f"{getdate()}")
   print(f"{newCity.city.capitalize()}\n")
   print(weatherCodes[newCity.weather])
   print(f"Minimum Temperature : {newCity.minTemp}")
   print(f"Maximum Temperature : {newCity.maxTemp}")


if __name__ == "__main__":
   main()
