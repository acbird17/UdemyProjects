import requests
from datetime import datetime

MY_LAT = 39.612652
MY_LONG = -105.016197

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(time_now)

print(sunrise)
print(sunset)