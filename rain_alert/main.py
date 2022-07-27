import requests
import os
from twilio.rest import Client


OWM_Endpoint =
api_key =

# twillio
account_sid =
auth_token =

weather_params = {
    'lat': 37.557245,
    'lon': 127.079558,
    'exclude': 'current,minutely,daily',
    'appid': api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json().get('hourly')

will_rain = False

for data in weather_data[:12]:
    # data = weather_data[i]
    if int(data.get('weather')[0].get('id')) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='',
        to='',
        body="It's going to rain today. Remember to bring an umbrella."
    )

    print(message.status)

