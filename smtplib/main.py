# import smtplib
# import json
#
# with open(file='env.json', mode='r') as file:
#     env = json.load(file)
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=env['email'], password=env['password'])
#     connection.sendmail(
#         from_addr=env['email'],
#         to_addrs='',
#         msg="Subject:Hello\n\nTHis is the body of my email.")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)

import datetime as dt
import random
import smtplib
import json

with open(file='env.json', mode='r') as file:
    env = json.load(file)


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:
    with open(file='quotes.txt', mode='r') as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=env['email'], password=env['password'])
        connection.sendmail(
            from_addr=env['email'],
            to_addrs='',
            msg=f'Subject:Quote\n\n{quote}'
        )
