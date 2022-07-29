import datetime
import random
import smtplib

now = datetime.datetime.now()
day = now.weekday()
data = open("quotes.txt")
new_data = data.readlines()
quote = random.choice(new_data)

username = "arghyadeepwish@gmail.com"
password = "4N5D3#ZYW+U7kK)"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=username, password=password)
    connection.sendmail(from_addr=username, to_addrs="jishuadhikary2015@gmail.com",
                        msg=f"Subject:Motivation\n\n{quote}")
    connection.close()
