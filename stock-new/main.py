import requests
import json
from twilio.rest import Client


## env
with open(file='env.json') as file:
    env = json.load(file)

# https: // www.alphavantage.co / query?function = TIME_SERIES_DAILY & symbol = IBM & apikey = demo

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla'

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

def get_daily_time_series():

    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_NAME,
        'apikey': env.get('ALPHA_VANTAGE_API_KEY')
    }

    response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()

    daily_data = data.get('Time Series (Daily)')
    daily_list = [value for (key, value) in daily_data.items()]

    return daily_list

def get_difference_percentage():
    daily_list = get_daily_time_series()

    yesterday_data = daily_list[0]
    yesterday_closing_price = float(yesterday_data.get("4. close"))

    day_before_yesterday_data = daily_list[1]
    day_before_yesterday_closing_price = float(day_before_yesterday_data.get('4. close'))

    difference = yesterday_closing_price - day_before_yesterday_closing_price
    if difference < 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    difference = abs(difference)
    diff_percentage = round((difference / yesterday_closing_price) * 100)



    print(yesterday_closing_price, day_before_yesterday_closing_price)
    print(diff_percentage)

    return diff_percentage, up_down
    # if diff_percentage > 0.1:
    #     print("Get News")

def get_news():
    news_params = {
        'apiKey': env.get('NEWS_API_KEY'),
        'q': COMPANY_NAME,
        'searchIn': 'title'
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    return news_response.json().get('articles')[:3]

def summarize_news(news):
    return [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article.get('title')}. \nBrief: {article.get('description')}" for article in news]

if __name__ == '__main__':
    client = Client(env.get('TWILIO_ACCOUNT_SID'), env.get('TWILIO_AUTH_TOKEN'))

    diff_percentage, up_down = get_difference_percentage()

    if diff_percentage >= 0:
        news = get_news()
        formatted_news = summarize_news(news)

        for article in formatted_news:
            message = client.messages.create(
                body=article,
                messaging_service_sid='MGac8bd642e484bfb84cdd0324a33619a3',
                to="+821049187971"
            )
