import smtplib
import datetime as dt
import random as rd
import keyring

my_email = "learnpythonsmtp@gmail.com"
recipient_email = "learnpythonsmtp@yahoo.com"
password = keyring.get_password("smtpgmail", "learnpythonsmtp@gmail.com")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("Intermediate+/32 Birthday Emails/quotes.txt", "r") as file:
        quotes = file.readlines()

    quotes = [quote.strip() for quote in quotes]
    random_quote = rd.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Quote of the day\n\n{random_quote}",
        )
