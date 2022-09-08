import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
LAT = 39.626166
LON = -105.084861
API = "aa4420eedeb1d9811827bbeefd8042fb"
account_sid = "ACeb256ff925abbed78254826a50446628"
auth_token = "062b27ac412c432c2c8a0322e7179ca8"


parameters = {
    "lat": LAT,
    "lon": LON,
    "units": "imperial",
    "appid": API,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
hourly_slice = data["hourly"][:12]

will_rain = False

for hour_data in hourly_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 600:
        will_rain = True
        
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain today.",
            from_='+16188364505',
            to='+18479122545'
        )
    print(message.status)