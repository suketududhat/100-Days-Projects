import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/suk2d/.env.txt")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

headers = {"x-app-id": NUTRITIONIX_APP_ID, "x-app-key": NUTRITIONIX_API_KEY}

user_input = input("Please enter exercise query: ")
input_params = {"query": user_input}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    headers=headers,
    json=input_params,
)
response.raise_for_status()
print(response.text)
