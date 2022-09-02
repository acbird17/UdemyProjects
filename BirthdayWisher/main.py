import smtplib
import random
import datetime as dt
import pandas

PLACEHOLDER = "[NAME]"

my_email = "acbird.ab@gmail.com"
password = "jayfbkyldsxxmrhy"

data = pandas.read_csv("./birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

now = dt.datetime.now()
now_tuple = (now.month, now.day)

if now_tuple in birthday_dict:
    birthday_name = birthday_dict[now_tuple]
    letter_template = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_template) as letter:
        content = letter.read()
        content = content.replace(PLACEHOLDER, birthday_name["name"])
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=birthday_name["email"], 
                            msg=f"Subject:Happy Birthday\n\n{content}.")

# date_of_birth = dt.datetime(year=1989, month=8, day=10)

