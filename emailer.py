# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 00:32:05 2022

@author: Kyle

important pre-req! You need to edit your permissions in gmail to allow unsecure apps, and need to request an app password for your mail.
"""

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

gmail_user = os.getenv('gmail_user')
gmail_pwd = os.getenv('gmail_pwd')

# Get image
path = r"C:\Users\Kyle\Downloads\denver_boulder_crop.jpg"

file = open(path, 'rb')

msgImage = MIMEImage(file.read())

file.close()

msgImage.add_header('Content-ID', '<image1>')  

# Draft Email

sent_from = gmail_user

to = [gmail_user]

message = MIMEMultipart("alternative")
message["Subject"] = 'Python Email Testing at ' + datetime.now().strftime('%H:%M:%S')
message["From"] = sent_from
message["To"] = ", ".join(to)

text = 'Please find the super important content below.\n\nThanks,\n\nKyle'

html = """\
    <html>
    <body>
    <p>Hi,<br><br>
    Please find the <strong>super</strong> important content below.<br><br><img src=cid:image1 alt="Today's Report"><br><br>Thanks,<br>Kyle</p>
    </body>
    </html>
    """
    
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)
message.attach(msgImage)



try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(gmail_user, gmail_pwd)
    server_ssl.sendmail(sent_from, to, message.as_string())
    server_ssl.close()
except:
    print('something went wrong with auth')