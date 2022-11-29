import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/suk2d/.env.txt")
pixela_token = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = "suketu"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": " ",
    "type": "int",
    "color": "sora",
}
headers = {"X-USER-TOKEN": pixela_token}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

graph1_endpoint = f"{graph_endpoint}/graph1"
pixel_params = {"date": "20221125", "quantity": "1"}
response = requests.post(url=graph1_endpoint, json=pixel_params, headers=headers)
print(response.text)
