#
# Send a spoofed email.  Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@gmail.com
# Recipient needs to be zultron@thebigeye.com
#

import smtplib

sender = 'bob-roswell-1947@gmail.com'
receivers = ['zultron@thebigeye.com']

message = """From: From Person <bob-roswell-1947@gmail.com>
To: To Person <zultron@thebigeye.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
  smtpObj = smtplib.SMTP('127.0.0.1', 1025)
  smtpObj.sendmail(sender, receivers, message)         
  print("Successfully sent email")
except SMTPException:
  print("Error: unable to send email")