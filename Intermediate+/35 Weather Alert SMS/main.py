import requests
import json
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/suk2d/.env.txt")
api_key = os.getenv("OWM_API_KEY")
MY_LAT = 0  # Your latitude
MY_LONG = 0  # Your longitude

# # Getting data from Weather Map API
# parameters = {
#     "lat": MY_LAT,
#     "lon": MY_LONG,
#     "appid": api_key,
#     "units": "imperial",
#     "exclude": "current,minutely,daily,alerts",
# }
# response = requests.get(
#     "https://api.openweathermap.org/data/3.0/onecall", params=parameters
# )
# response.raise_for_status()
# data = response.json()

# # dumping data to JSON to limit querying
# with open("100-Days-Projects/Intermediate+/35 Weather Alert SMS/data.txt", "w") as file:
#     json.dump(data, file, indent=4)


def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot_chatID = os.getenv("TELEGRAM_CHAT_ID")
    print(bot_token)
    print(bot_chatID)
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


with open("100-Days-Projects/Intermediate+/35 Weather Alert SMS/data.txt") as file:
    data = json.load(file)

hourly_data = data["hourly"]

for n in range(12):
    weather_id = hourly_data[n]["weather"][0]["id"]
    if weather_id < 700:
        telegram_bot_sendtext("You will need an umbrella!")
        break
