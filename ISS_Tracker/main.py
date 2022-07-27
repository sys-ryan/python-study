import requests
from datetime import datetime
import json
import smtplib`
import time


MY_LAT = 37.553235
MY_LONG = 127.071936

## env variables
with open(file='env.json') as file:
    env = json.load(file)


def is_iss_overhaed():
    global iss_lat, iss_lng
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data.get('iss_position').get('latitude'))
    iss_lng = float(data.get('iss_position').get('longitude'))

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_lng <= MY_LONG-5:
        return True


def is_nignt():

    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data.get('results').get('sunrise')
    sunset = data.get('results').get('sunset')

    sunrise = int(sunrise.split('T')[1].split(':')[0])
    sunset = int(sunset.split('T')[1].split(':')[0])

    time_now = int(datetime.now().hour)

    if time_now >= sunset or time_now <= sunrise: # dark
        return True

while True:
    print(datetime.now())
    if is_iss_overhaed() and is_nignt():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=env['email'], pasword=env['password'])
        connection.sendmail(
            from_addr=env['email'],
            to_addrs=env['email'],
            msg='Subject:Loook Up👆\n\nThe ISS is above you in the sky!'
        )

    time.sleep(60)






