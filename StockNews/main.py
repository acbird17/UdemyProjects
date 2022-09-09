import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime
import math
from dotenv import load_dotenv

load_dotenv()
 
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
DATE = datetime.date.today()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": os.getenv("ALPHA_API_KEY"),
}

news_params = {
    "q": COMPANY_NAME,
    "from": DATE,
    "sortBy": "popularity",
    "apiKey": os.getenv("NEWS_API_KEY"),
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list =[value for (key,value) in stock_data.items()]

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
news_slice = news_data["articles"][:3]

yesterday_stock_close = int(float(stock_data_list[0]["4. close"]))
day_prior_stock_close = int(float(stock_data_list[1]["4. close"]))
stock_abs = abs(yesterday_stock_close - day_prior_stock_close)
stock_difference = math.floor(((yesterday_stock_close - day_prior_stock_close)/((yesterday_stock_close + day_prior_stock_close)/2)) * 100)

up_or_down = None
if stock_difference > 0:
    up_or_down = "🔺"
else:
    up_or_down = "🔻"

if stock_difference > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_slice = news_data["articles"][:3]
    format_articles = [f"{STOCK_NAME}: {up_or_down}{stock_difference}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in news_slice]
    
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    
    for article in format_articles:
        message = client.messages.create(
            body=article,
            from_=os.getenv("TWILIO_NUMBER"),
            to=os.getenv("TO_NUMBER")
        )
    print(format_articles)