#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 12: Debugging (Lesson 35-37)

# import traceback for traceback.format_exc() function for Lesson 35 The raise and assert Statements
# import logging for logging.basicConfig() function for Lesson 36 Logging

print('#########################################################')
print('### Lesson 35. The raise and assert Statements')
print('#   STARTS HERE')
print('')

# Instead of using try and except for exceptions you antipate, you can raise your own exceptions in your code
# "Raising Your Own Exceptions"
# Stop running code in this function and move the program execution to the except statement
# exceptions are raised with a Raise statement
# import traceback for traceback.format_exc() function

import traceback

"""
Printing a rectangle with specified symbol, width, and height
"""
"""
#Without error handling
def boxPrint(symbol,width,height):
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)
"""


def boxPrint(symbol, width, height):

    # Error handling by confirming valid input
    if len(symbol) != 1:
        try:
            raise Exception('Symbol must be of length one')
        except:
            errorfile = open('autoDemo-DebuggingErrorLog.txt','a')
            errorfile.write(traceback.format_exc())
            errorfile.close()
            print('See autoDemo-DebuggingErrorLog.txt for invalid input error') #not appropriate for user experience, probably best for dev only messaging?

    if (width < 2) or (height < 2):
        try:
            raise Exception('Width and Height must be at least 2')
        except:
            errorfile = open('autoDemo-DebuggingErrorLog.txt', 'a')
            errorfile.write(traceback.format_exc())
            errorfile.close()
            print('See autoDemo-DebuggingErrorLog.txt for invalid input error')  # not appropriate for user experience, probably best for dev only messaging?

    # Now for the action
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('333',10,10)

# use traceback.format_exc() function to get Traceback text as a string value

# raise Exception('This is my error message.')

# if there are no Try and Except statements covering the Raise statment, the program crashes and displays the Exception message


# The Assert Statement
# Assertion is a sanity check to confirm code isn't doing any Known Wrongs
# Sanity checks are performed by Assert statements
# if assert False, then generate message
## COMMENTED THE NEXT LINE OUT TO ALLOW FOR OTHER LESSON TO RUN
#assert False, '\nThis is the error message to indicate the Assertion wasn\'t met.\n'
# Unlike try and except, an assert statement is a case where you want your program to crash to Fail Fast
# These are for Programmer Errors, NOT user errors, and not meant to be recovered from; instead, need to fix the code
# whereas you would Raise Exceptions for errors you can recover from, like File Not Found or allowing the user to provide excepted input

print('### Lesson 35. ')
print('#   ENDS HERE')
print('#########################################################')
print('')


print('#########################################################')
print('### Lesson 36. Logging')
print('#   STARTS HERE')
print('')

# import logging for logging.basicConfig() function
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Above can log to file (instead of on screen) using an extra "filename" argument in the beginning:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL) #Disable logging at critical (highest) and lower, effectively disabling all logging
# 5 Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

print('Nothing actually outputted unless logging is enabled at some level using the commented out "logging.disable() line above')

logging.debug('Start of program')
i = 2
i = i + 2
logging.debug('simple sample of whatever the percent s means which has a value of %s' % (i))
j = i * i
logging.debug('oh, I get what the percent s means now that you can have multiple values shown by action on i which is %s captured in j which is %s' % (i,j))
logging.debug('End of program')

print('')
print('### Lesson 36. ')
print('#   ENDS HERE')
print('#########################################################')
print('')


print('#########################################################')
print('### Lesson 37. Using the debugger')
print('#   STARTS HERE')
print('')

print('Just took notes in comments')
print('')

# Debugger is a feature of IDLE
# allows running code one line at a time

# reveals "dunder variables" beyond scope of course

# use Over button to go through each line of code

# Go runs to end of until Breakpoint (use right-click to access it in IDLE)

# Step moves into a function call

# Out continues until function call returns

print('### Lesson 37. ')
print('#   ENDS HERE')
print('#########################################################')
print('')