##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
list = data.to_dict(orient="records")
letter1 = "letter_1.txt"
letter2 = "letter_2.txt"
letter3 = "letter_3.txt"
letters = [letter1, letter2, letter3]
# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
day = now.day
month = now.month


def check():
    for item in list:
        if item["month"] == month and item["day"] == day:
            data = open(random.choice(letters))
            rand_letter = data.read()
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
            # person's actual name from birthdays.csv
            rand_letter = rand_letter.replace("[NAME]", item["name"])
            # 4. Send the letter generated in step 3 to that person's email address.
            username = "arghyadeepwish@gmail.com"
            password = "4N5D3#ZYW+U7kK)"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=username, password=password)
                connection.sendmail(from_addr=username, to_addrs=item["email"],
                                    msg=f"Subject:Happy Birthday\n\n{rand_letter}")
                connection.close()


check()
