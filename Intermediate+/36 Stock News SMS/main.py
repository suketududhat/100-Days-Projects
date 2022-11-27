import requests
import json
from datetime import datetime, date
import os
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv("C:/Users/suk2d/.env.txt")
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")


def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot_chatID = os.getenv("TELEGRAM_CHAT_ID")
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()


def get_stock_price(STOCK):
    stock_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": stock_api_key,
        "units": "imperial",
        "exclude": "current,minutely,daily,alerts",
    }
    response = requests.get(
        "https://www.alphavantage.co/query", params=stock_parameters
    )
    response.raise_for_status()
    stock_data = response.json()

    with open(
        "100-Days-Projects/Intermediate+/36 Stock News SMS/stock_data.txt", "w"
    ) as file:
        json.dump(stock_data, file, indent=4)


# get_stock_price(STOCK)

with open("100-Days-Projects/Intermediate+/36 Stock News SMS/stock_data.txt") as file:
    stock_data = json.load(file)
    stock_data = stock_data["Time Series (Daily)"]
    stock_data_list = list(stock_data.items())

# print(stock_data_list[0][1]["4. close"])
today = datetime.now()
yesterday = date(today.year, today.month, today.day - 1)
before_yesterday = date(yesterday.year, yesterday.month, yesterday.day - 1).strftime(
    "%Y-%m-%d"
)
yesterday = yesterday.strftime("%Y-%m-%d")

# print(stock_data[before_yesterday]["4. close"])


def get_news(STOCK):
    news_parameters = {
        "apikey": news_api_key,
        "q": STOCK,
    }
    response = requests.get(
        "https://newsapi.org/v2/top-headlines", params=news_parameters
    )
    response.raise_for_status()
    news_data = response.json()

    with open(
        "100-Days-Projects/Intermediate+/36 Stock News SMS/news_data.txt", "w"
    ) as file:
        json.dump(news_data, file, indent=4)


# get_news(STOCK)

with open("100-Days-Projects/Intermediate+/36 Stock News SMS/news_data.txt") as file:
    news_data = json.load(file)

articles_list = news_data["articles"]


for n in range(len(articles_list)):
    message = f"{STOCK}: \nHeadline: {articles_list[n]['title']} \nBrief: {articles_list[n]['description']}"
    # print(message)
# telegram_bot_sendtext(message)
