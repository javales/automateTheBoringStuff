# /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 15: Email (Lesson 46-47) - only Lesson 46 - Sending Emails

# Native module smtplib to send mail

import smtplib

# Create Connection object

conn = smtplib.SMTP('smtp.gmail.com', 587)
print('This is the connection object:')
print(conn)
print('And the object type:')
print(type(conn))
print('')
print('Call conn.ehlo() to start the connection')
print(conn.ehlo())
print('')

print('Start TLS:')
print(conn.starttls())
print('')

print('Start login:')
print(conn.login('sunnyvale.ryder@gmail.com','spmkqrhopvghpdvv'))

print('Sending Mail:')
print(conn.sendmail('sunnyvale.ryder@gmail.com','jimmyvales@gmail.com','Subject: You got mail!\n\nHey,\nThis is a bot, one last-last time!'))
print('')
#blank dictionary {} back from conn.sendmail() means success

# Log out of connection
print('Logging out of connection:')
print(conn.quit())
print('')