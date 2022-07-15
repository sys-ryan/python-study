##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import json
import pandas

### load environment variables
with open(file='env.json', mode='r') as file:
    env = json.load(file)

# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
print(data)
print()

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day

today_birthday = data[(data.month == current_month) & (data.day == current_day)]
today_birthday_email_list = today_birthday.email.to_list()

if len(today_birthday_email_list) > 0:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=env['email'], password=env['password'])

        for email in today_birthday_email_list:
            file_num = random.choice([1, 2, 3])
            with open(file=f'./letter_templates/letter_{file_num}.txt') as file:
                contents = file.read()
                name = today_birthday[today_birthday.email == email].name.values[0]
                contents = contents.replace("[NAME]", name)
            message = f'Subject:Happy Birthday!\n\n{contents}'

            connection.sendmail(
                from_addr=env['email'],
                to_addrs=email,
                msg=message
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





