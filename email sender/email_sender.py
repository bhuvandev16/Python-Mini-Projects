import smtplib
import time
from email.message import EmailMessage
import ssl

email_sender = str(input('Enter your email address : '))
email_password = '{enter your app password}' #NOTE: Doesn't work with email password
email_receiver = str(input('Enter receiver email address : '))
subject = str(input("What's the subject :  "))
message = str(input("What's the message : "))
time_limit_needed = str(input('Do you want to set time limit (y/n) : '))
time_limit = 0

msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = email_sender
msg['To'] = email_receiver
msg.set_content(message)


def email_sent():
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_server:
        smtp_server.login(email_sender, email_password)
        smtp_server.sendmail(email_sender, email_receiver, msg.as_string())


if time_limit_needed == 'y':
    time_limit_value = int(input('Enter the time limit in seconds : '))
    time_limit_value = time_limit
    time.sleep(time_limit)
else:
    print("Email senting")


email_sent()
print('Message sent')