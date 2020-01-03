#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 13: Web Scraping (Lesson 38-41) - only Lesson 38 - The webbrowser Module

# Will also enable command line argument option, so include sys in addition to webbrowser module
# the command line arguments are delimited by spaces within sys.argv

import webbrowser, sys, pyperclip

# First see if command line arguments were passed

if len(sys.argv) > 1:
    # capture address entered as an argument when running the script
    searchTerm = ' '.join(sys.argv[1:]) # start the slice at index 1 to ignore the script name in index 0
else:
    searchTerm = pyperclip.paste()

webbrowser.open('https://www.dogpile.com/serp?q='+searchTerm)

#webbrowser.open('https://app.pluralsight.com/')

# In Windows, you'd create a batch file with @py.exe c:\path\to\script.py %*
# the %* allows passing arguments from the batch call to the py script called by the batch file
