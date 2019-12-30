#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 10: Regular Expressions (Lesson 23-29)

### 23. Regular Expression Basics
#################################

print('++++++++++++++++++++++++++++++++++++')
print('Lesson 23. Regular Expression Basics')
print('starts here')
print('------------------------------------')
print('')

#Import Regex re module to access regex functions
import re

#The string to be examined
numbersHere='Call me 415-444-3343 tomorrow, or 505-333-3333 the next day'

#Create a regex object and assign to variable
phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')

#Access the regex object's search() method capturing either Match object or None in a match object variable
matchObject = phoneNumRegex.search(numbersHere)

#When there is match, you can access the matching string with the match object's group() method
print('First phone number found using search() method:\n' + matchObject.group())
print('')

#To access all matches in the match object variable, use findall
print('All phone numbers found using findall() method:')
print(phoneNumRegex.findall(numbersHere))
print('')

print('------------------------------------')
print('Lesson 23. Regular Expression Basics')
print('ends here')
print('++++++++++++++++++++++++++++++++++++')
print('')

### 24. Regex Groups and the Pipe Character
###########################################

print('++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson 24. Regex Groups and the Pipe Character')
print('starts here')
print('----------------------------------------------')
print('')

#Import Regex re module to access regex functions
import re

#The string to be examined
numbersHere='human enters text here'

print('----------------------------------------------')
print('Lesson 24. Regex Groups and the Pipe Character')
print('ends here')
print('++++++++++++++++++++++++++++++++++++++++++++++')
print('')