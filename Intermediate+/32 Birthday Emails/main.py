import pandas as pd
import random as rd
import smtplib
import datetime as dt
import keyring

##################### Extra Hard Starting Project ######################

my_email = "learnpythonsmtp@gmail.com"
recipient_email = "learnpythonsmtp@yahoo.com"
password = keyring.get_password("smtpgmail", "learnpythonsmtp@gmail.com")

# 1. Update the birthdays.csv

df = pd.read_csv("100-Days-Projects/Intermediate+/32 Birthday Emails/birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

# Picks a birthday person based on current month and today
birthday_person = df[(df.month == month) & (df.day == day)]

# Put letter templates in a list
letter_list = []
for n in range(1, 4):
    with open(
        f"100-Days-Projects/Intermediate+/32 Birthday Emails/letter_templates/letter_{n}.txt"
    ) as file:
        letter_list.append(file.read())


try:
    if birthday_person.month.item() == month:
        letter = rd.choice(letter_list)
        letter = letter.replace("[NAME]", f"{birthday_person.name.item()}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg=f"Subject:Happy Birthday!\n\n{letter}",
            )
except ValueError:
    None

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
