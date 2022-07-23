import requests

quize_url = 'https://opentdb.com/api.php?amount=10&type=boolean'
parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url=quize_url, params=parameters)
response.raise_for_status()
question_data = response.json().get('results')

