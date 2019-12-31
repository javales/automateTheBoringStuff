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

#Imported Regex re module to access regex functions above already
stringPlay = 'My number is 415-555-4334'
stringPlay2 = 'My number is (415)-444-3333'

#Groups are specified by parentheses
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject2 = phoneNumRegex2.search(stringPlay)

phoneNumRegex3 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
matchObject3 = phoneNumRegex3.search(stringPlay2)

print('Entire match group:')
print(matchObject2.group())
print('Just the first group:')
print(matchObject2.group(1))
print('')
print('Print regex object output that accounts for parentheses in text')
print(matchObject3.group())
print('')

#Use pipe to match any one of the specified options
stringPlay3 = 'Batmobile'
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject4 = batRegex.search(stringPlay3)
print('Printing pipe match for second half of Bat[one of four options]')
print(matchObject4.group())
print('')
print('Printing which of the matches caught in group() method')
print(matchObject4.group(1))
print('')

print('----------------------------------------------')
print('Lesson 24. Regex Groups and the Pipe Character')
print('ends here')
print('++++++++++++++++++++++++++++++++++++++++++++++')
print('')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson 25. Repetition in Regex Patterns and Greedy/Nongreedy Matchin')
print('STARTS HERE')
print('--------------------------------------------------------------------')
print('')

#Matching a *specific* number of repititions

#Imported Regex re module to access regex functions above already

stringPlay4 = 'My number is 415-555-4334'
stringPlay5 = 'My number is 444-3333'

#Make the first group matched optional with question mark for either 0 or 1 times matched
phoneNumRegex4 = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
matchObject5 = phoneNumRegex4.search(stringPlay4)
matchObject6 = phoneNumRegex4.search(stringPlay5)
print('Print the usual full number as expected')
print(matchObject5.group())
print('')
print('Just the last seven digits since no area code was specified and optional in this regex object')
print(matchObject6.group())
print('')

#The star * character means match zero or more times
stringPlayBat = 'Batwoman'
stringPlayBat2 = 'Batwowowoman'

print('The expected simple match using question mark ? character')
batRegex2 = re.compile(r'Bat(wo)?man')
matchObject7 = batRegex2.search(stringPlayBat)
print(matchObject7.group())
print('')

print('The repeating match using star * character')
batRegex3 = re.compile(r'Bat(wo)*man')
matchObject8 = batRegex3.search(stringPlayBat2)
print(matchObject8.group())
print('')

#The plus + character means must match ONE or more times
stringPlayBat3 = 'Batwoman'
stringPlayBat4 = 'Batman'

batRegex4 = re.compile(r'Bat(wo)+man')
matchObject7 = batRegex4.search(stringPlayBat3)
matchObject8 = batRegex4.search(stringPlayBat4)

print('The expected match since at least match of "wo" group exists mandated by + character')
print(matchObject7.group())
print('')
print('No match here because Batman does not meet the mandated + "wo"')
print(matchObject8)
print('')

#Can escape +*? with \
stringEscape = '"I learned about +*?+*? regex escape syntax"'

escapeRegex = re.compile(r'(\+\*\?)+')
matchObject9 = escapeRegex.search(stringEscape)
print('The string is ' + stringEscape)
print('This confirmed in above string')
print(matchObject9.group())
print('')

#Curly braces {x} mandate matching the string x number of times
exactnumString = 'HaHaHa'
exactnumRegex = re.compile(r'(Ha){3}')
matchObject10 = exactnumRegex.search(exactnumString)
print('Found a match of HaHaHa')
print(matchObject10.group())
print('')

#Curly braces {x,y} mandate matching the string between x and y number of times
exactnumStringRange = 'HaHaHaHa'
exactnumRegex = re.compile(r'(Ha){3,5}')
matchObject10 = exactnumRegex.search(exactnumStringRange)
print('Found a match of HaHaHaHa which is between 3 and 5 Ha\'s')
print(matchObject10.group())
print('')

exactnumStringRange2 = 'HaHaHaHaHaHaHa'
exactnumRegex = re.compile(r'(Ha){3,5}')
matchObject10 = exactnumRegex.search(exactnumStringRange2)
print('Found a match of only the first 5 Ha\'s which is within the upper limit of 3 and 5 Ha\'s')
print(matchObject10.group())
print('')

exactnumStringRange = 'HaHaHaHa'
exactnumRegex = re.compile(r'(Ha){3,5}')
matchObject10 = exactnumRegex.search(exactnumStringRange)
print('Found a match of HaHaHaHa which is between 3 and 5 Ha\'s')
print(matchObject10.group())
print('')
print('And when leaving 3 or 5 out, then it\'s going to be (0 to 5) or (3 to unbounded) number of occurrences')
print('')

#By default, regex does Greedy matches of the upper bound of the range
greedyDigits = '1234567'
digitRegex = re.compile(r'(\d){3,5}')
matchObject11 = digitRegex.search(greedyDigits)
print('From string 1234567, the range 3 to 5 prints this greedy match despite lower limit of 3')
print(matchObject11.group())
print('It\'s matching the longest possible string that matches the regex object\'s specified pattern')
print('')

#Use a question mark ? after the curly brace to make it Not Greedy
digitRegex = re.compile(r'(\d){3,5}?')
matchObject11 = digitRegex.search(greedyDigits)
print('From string 1234567, the range 3 to 5 prints this Non Greedy match by use of the question mark character after curly brace')
print(matchObject11.group())
print('It\'s matching the smallest possible string that matches the regex object\'s specified pattern')
print('')

print('---------------------------------------------------------------------')
print('Lesson 25. Repetition in Regex Patterns and Greedy/Nongreedy Matching')
print('ENDS HERE')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson 26. Regex Character Classes and the findall() Method')
print('STARTS HERE')
print('-----------------------------------------------------------')
print('')

#findall() finds ALL matches, not just the first like the search() method and returns them as list of strings or list of tuples of strings

#if there is Zero or One group, it returns a List of Strings
resume = '333-333-2222 and then that then another 333-344-5555'
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject12 = phoneRegex.findall(resume)
print('findall() returns a list of strings when there is 0 or 1 grouping of string patterns like so')
print(matchObject12)
print('')

#if there are Two or More groups, it returns a List of Tuples of Strings
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
matchObject12 = phoneRegex.findall(resume)
print('findall() returns a list of tuples representing each collection of those matching strings like so')
print(matchObject12)
print('')

#Character Classes
#\d vs \D NOT a numeric digit
#\w vs \W word character excluding spaces but including underscores
#\s vs \S

lyrics = '12 drummers drumming 3 dumb_drummers drueling'
xmasRegex = re.compile(r'\d+\s\w+')
matchObject13 = xmasRegex.findall(lyrics)
print('Matching one or more digits followed by a space followed by one more word characters')
print(matchObject13)
print('')

#Making your own character classes using square brackets
roboString = 'Robocop eats baby food'
roboString2 = 'FabioCop eats fake bagels'
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex2 = re.compile(r'[a-fA-F]')
matchObject14 = vowelRegex.findall(roboString)
matchObject15 = vowelRegex2.findall(roboString2)
print('Matching against own flat list of character class letters')
print(matchObject14)
print('Matching against a own ranged list of character class letters')
print(matchObject15)
print('')

#Find two characters in a row using the curly brackets after the character class definition
vowelRegex3 = re.compile(r'[aeiouAEIOU]{2}')
matchObject16 = vowelRegex3.findall(roboString2)
print('Matching any two matching characters in a row from roboString2')
print(matchObject16)
print('')

#Negative Character Classes matching EVERYTHING that ISN'T in the character class
vowelRegex4 = re.compile(r'[^aeiouAEIOU]')
matchObject17 = vowelRegex4.findall(roboString2)
print('Matching everything NOT in the vowelRegex4 character using the Negative Character Class ^ character')
print(matchObject17)
print('')

print('-----------------------------------------------------------')
print('Lesson 26. Regex Character Classes and the findall() Method')
print('ENDS HERE')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')