import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')

response.raise_for_status()

data = response.json()['iss_position']
print(data)

iss_position = (data.get('longitude'), data.get('latitude'))
print(iss_position)


url = 'http://api.kanye.rest'