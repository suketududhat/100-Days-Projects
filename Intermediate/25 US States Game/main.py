# with open("Intermediate/25 US States Game/weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# print(data)

import pandas

df = pandas.read_csv("Intermediate/25 US States Game/weather_data.csv")
temps = df["temp"].to_list()
print(df["temp"].mean())
