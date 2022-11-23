import requests
from datetime import datetime, timezone
import keyring
import smtplib

my_email = "learnpythonsmtp@gmail.com"
recipient_email = "learnpythonsmtp@yahoo.com"
password = keyring.get_password("smtpgmail", my_email)

MY_LAT = 33.787914  # Your latitude
MY_LONG = -117.853104  # Your longitude


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_iss_over_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # iss_latitude = MY_LAT
    # iss_longitude = MY_LONG
    if (
        iss_latitude > (MY_LAT - 5)
        and iss_latitude < (MY_LAT + 5)
        and iss_longitude > (MY_LONG - 5)
        and iss_longitude < (MY_LONG + 5)
    ):
        return True
    else:
        return False


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(timezone.utc)
    hour_now = time_now.hour
    # hour_now = 12
    if hour_now <= sunrise and hour_now >= sunset:
        return True
    else:
        return False


if is_iss_over_me() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg="Subject:ISS Overhead!\n\nLook up now!",
        )
