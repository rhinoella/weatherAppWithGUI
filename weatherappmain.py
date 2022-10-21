from datetime import date
from CityWeather import CityWeather


# uses datetime to get the date
def getdate():
   dateToday = date.today()
   return dateToday


def main():
   newCity = CityWeather()
   geocoding = newCity.getinput()
   newCity.getgeocode(geocoding)
   newCity.getweather()
   print(f"{getdate()}")
   print(f"{newCity.city.capitalize()}\n")
   print(newCity.weatherCodes[newCity.weather])
   print(f"Minimum Temperature : {newCity.minTemp}")
   print(f"Maximum Temperature : {newCity.maxTemp}")


if __name__ == "__main__":
   main()
