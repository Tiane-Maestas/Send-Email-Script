import smtplib, ssl
from datetime import datetime
import time

#Creates instances of email information
sender_email = "TITLE"
receiver_email = "TITLE"
#the two \n is neccessarry to inssure the body is in the correct place
message = """\
Subject: Your Daily Reminder

I Love You."""

port = 465  # For SSL
password = input("Type your password and press enter: ")

#Ex time: "23:30"
targetTime = "TIME"

#waits until the right time before creating a secure conection so you don't get logged out
print("Begining Time Check...")
run = True
while run:
    #if input("Type command:") == 'S':
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    print("Last Time Check =", currentTime)
    if currentTime == targetTime:
        run = False
        print("Time met!")
        continue
    print("Sleeping...")
    time.sleep(30)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Messege Sent.")