weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {
    weekday: round((temp * (9 / 5) + 32), 1) for (weekday, temp) in weather_c.iterrows()
}


print(weather_f)
