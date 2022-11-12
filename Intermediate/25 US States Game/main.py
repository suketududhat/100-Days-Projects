import pandas as pd

df = pd.read_csv(
    "Intermediate/25 US States Game/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

# temps = df["temp"].to_list()
# print(df["temp"].mean())

fur_colors = df["Primary Fur Color"].unique().tolist()
fur_colors.pop(0)
count = []

for color in fur_colors:
    squirrels = (df["Primary Fur Color"] == color).sum()
    count.append(squirrels)


df_count = pd.DataFrame(columns=["Fur Color", "Count"])
df_count["Fur Color"] = fur_colors
df_count["Count"] = count
print(df_count)

df_count.to_csv("Intermediate/25 US States Game/squirrel_count.csv")
