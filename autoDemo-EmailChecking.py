# /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 15: Email (Lesson 46-47) - only Lesson 47 - Checking Email

# Native IMAPLIB module is for checking email, but NOT going to use that for this lesson
# instead install two third-party modules using pip install imapclient and pip install pyzmail36
# must use pyzmail36 for Python 3 per tip in Q&A
# must set SSL context per tip in Q&A on CERTIFICATE_VERIFY_FAILED error (Instructor suggested: https://stackoverflow.com/questions/25318012/how-to-connect-with-python-imap4-ssl-and-self-signed-server-ssl-cert)

import imapclient
import pyzmail
import socket
import ssl

SetSSLContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Create Connection object
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True, ssl_context=SetSSLContext)
print('This is the connection object:')
print(conn)
print('And the object type:')
print(type(conn))
print('')

print('Start login:')
print(conn.login('sunnyvale.ryder@gmail.com','*********'))
print('')

print('Connect to Inbox folder:')
print(conn.select_folder('INBOX', readonly=True))
print('')

print('Find message UIDs since 1/12/2020...')
#print(conn.search(['SINCE 12-Jan-2020'])) #DOESN'T WORK, SO FOUND BELOW Q&A TIP:
print(conn.search(['SINCE', '12-Jan-2020'])) #Aside from SINCE, can search against ALL, BEFORE, ON, SUBJECT, BODY, TEXT, and other search terms that are from the older IMAP days
print('')


rawMessage = conn.fetch([17],['BODY[]','FLAGS'])
print('Printing Raw Message:')
print(rawMessage)
print('')

Message = pyzmail.PyzMessage.factory(rawMessage[17][b'BODY[]'])
print('Printing Pyzmail Message Subject:')
print(Message.get_subject())
print('')
print('Printing Pyzmail Message Addresses From:')
print(Message.get_addresses('from'))
print('')
print('Printing Pyzmail Message Addresses To:')
print(Message.get_addresses('to'))
print('')
print('Printing Pyzmail Message Addresses Bcc:')
print(Message.get_addresses('bcc'))
print('')

#text_part member variable tells you if just text email or not
print('Is this just a text email or not?')
print('Printing Text Part, if any:')
print(Message.text_part)
print('')
print('Printing HTML Part, if any:')
print(Message.html_part)
print('')

#get main message of email using get_payload() method
MessageTextTest = Message.text_part.get_payload().decode('UTF-8') #UTF-8 encoding can be used "99%" of the time
print('Attempt at displaying message:')
print(MessageTextTest)
print('')

#list IMAP folders
foldersObj = conn.list_folders()
print('These are the account\'s folders:')
print(foldersObj)
print('')

#delete the forPython folder
selectForPython = conn.select_folder('INBOX', readonly=False)
print('Deleting message with UID 17:')
print(conn.delete_messages(17))
print('')

# Log out of connection
print('Logging out of connection:')
#print(conn.quit())
print(conn.logout())
print('')

# More Documentation:
# https://imapclient.readthedocs.org
# http://www.magiksys.net/pyzmail
# https://automatetheboringstuff.com/chapter16