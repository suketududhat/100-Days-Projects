# with open("Intermediate/25 US States Game/weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# print(data)

import pandas as pd

df = pd.read_csv(
    "Intermediate/25 US States Game/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

# temps = df["temp"].to_list()
# print(df["temp"].mean())

fur_colors = df["Primary Fur Color"].unique().tolist()


grey_squirrels = df.loc[df["Primary Fur Color"] == "Gray", ["Primary Fur Color"]]
grey_squirrels = grey_squirrels.count()
print(fur_colors)
