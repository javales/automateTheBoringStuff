#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 13: Web Scraping (Lesson 38-41) - only Lesson 39 - Downloading from the Web with the Requests Module

# install the third-party requests module FIRST to be able to IMPORT the requests module to download webpages and files

import requests

# response object returns the response from the web server for the get request
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# confirm request succeeded with status_code attribute of response object
# must convert to string first though
resStatus = res.status_code
print('')
print('Requested https://automatetheboringstuff.com/files/rj.txt')
print('Request Status: ' + str(resStatus))
print('')

# when successful, the web resource is stored as a string in the res.text variable
# must convert len(res.text to string to concat to output

lengthOfResObjectResource = len(res.text)
print('')
print('Requested resource length of https://automatetheboringstuff.com/files/rj.txt')
print('Resource Length: ' + str(lengthOfResObjectResource))
print('')

# use slice to print first 500 characters
print('Printing first 500 characters of above:')
print(res.text[:500])
print('')

# "Simpler" way to check for success is to call the raise_for_status() method on the response object
# res.raise_for_status() # raises exception if error during download, and nothing if fine
# use in a try and except

# Save the file to a file on your computer using Write-Binary Mode open(filename, 'wb')
playFile = open('RomeoAndJuliet.txt', 'wb')
#even though only text, you need to write in binary to preserve the unicode encoding of the text
#for more information: All About Python & Unicode: http://bit.ly/unipain
#this method works for ANY file you download using requests

# Now use iter_content() method on object to write to disk in chunks of size specified
print('Writing chunks to create file.')
for chunk in res.iter_content(100000): #each chunk is of a bytes data type, so specify number of bytes each chunk will contain
    playFile.write(chunk) #returns number of bytes written to file
print('')

playFile.close()
print('playFile closed')
print('')

#for more information: http://requests.readthedocs.org
#not the best use of requests when login is required or when URL is not known
#for that, another lesson
#Selenium lets you control the web browser *directly*