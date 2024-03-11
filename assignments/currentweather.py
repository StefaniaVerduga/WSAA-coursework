# Author: Stefania Verduga
# Module: Web Services and Applications
# Write a python program called currentweather.py that will print out the current temperature and the wind direction.

import requests
import json

# Get the temperature data from the url
url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
response = requests.get(url)
data = response.json()
#with open ("weatherdump.json", "w") as fp:
#    json.dump(data, fp)

current_temp = data["current"]["temperature_2m"]
print("The current temperature is:", current_temp, "°C")

# Get the wind data from the url
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url)
data = response.json()
#with open ("winddump.json", "w") as fp:
#    json.dump(data, fp)

current_wind = data["current"]["wind_speed_10m"]
print("The current wind speed is:", current_wind, "m/s")