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


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson 27. Regex Dot-Star and the Caret/Dollar Characters')
print('STARTS HERE')
print('-----------------------------------------------------------')
print('')

#Must begin with versus must end with
stringHell = ('Yeah Yeah Hello')
stringHello = ('Hello, Yeah')
beginsWithHelloRegex = re.compile(r'^Hello')
matchObject18 = beginsWithHelloRegex.search(stringHell)
matchObject19 = beginsWithHelloRegex.search(stringHello)
print('Didn\'t match since not starting with Hello')
print(matchObject18)
print('')
print('Matches since starting with Hello')
print(matchObject19.group())
print(matchObject19)
print('')

stringPlease = 'Some more, Please'
stringPleez = 'Oh Puh-leez'
regexPlease = re.compile(r'Please$')
matchObject = regexPlease.search(stringPlease)
print('Matching stringPlease since ending with Please')
print(matchObject.group())
print('From ' + '"' + stringPlease + '"')
print('')
matchObject = regexPlease.search((stringPleez))
print('Not matching stingPleez since no end Please')
print(matchObject)
print('From ' + '"' + stringPleez + '"')
print('')

#Combine both beginning with ending with
digitsAll = '1232132403'
digitsNotAll = '23423429d32342342'
allDigitsRegex = re.compile(r'^\d+$')
matchObject = allDigitsRegex.search(digitsAll)
matchObject2 = allDigitsRegex.search(digitsNotAll)
print('String does begin and end only with digits')
print(matchObject.group())
print('String does not begin and end only with digits due to letter in middle')
print(matchObject2)
print('')

#Period or dot stands for any SINGLE character EXCEPT for newline
catsString = 'The cat in the hat sat on the flat mat'
atRegex = re.compile(r'.at')
atRegexOneOrTwo = re.compile(r'.{1,2}at')
matchObject = atRegex.findall(catsString)
print('All matches for any string pattern ending in "at" but with only one character ahead')
print(matchObject)
print('From string "' + catsString + '" (notice how "flat" is not included)')
print('')

matchObject = atRegexOneOrTwo.findall(catsString)
print('All matches for any string pattern ending in "at" and with one or two characters ahead')
print(matchObject)
print('From string "' + catsString + '" (notice how spaces are included ahead in addition to flat)')
print('')



#Dot Star means ANYTHING because . is Anything But Newline while * is 0 or More
#so, "anything plus 0 or more of that anything"
#Greedy Matching
nameFirstLastString = 'First Name: Al Last Name: Stewart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
matchObject = nameRegex.findall(nameFirstLastString)
print('Pulling the First and Last Names out of "First Name: Al Last Name: Stewart"')
print(matchObject)
print('')

#Non-Greedy Matching
serve = '<I eat breakfast> and brunch.>'

nonGreedyRegex = re.compile(r'<(.*?)>')
matchObject = nonGreedyRegex.findall(serve)
print('Non-greedy match between <> using .*?')
print(matchObject)
print('')

GreedyRegex = re.compile(r'<(.*)>')
matchObject = GreedyRegex.findall(serve)
print('Greedy match between <> without ? at end')
print(matchObject)
print('')

#Force . to include newline using re.DOTALL argument
primeObjective = 'Robocop serves the public trust.\nProtects the innocent.\nUpholds the law.'
print(primeObjective)
print('')

dotStarRegex = re.compile(r'.*')
matchObject = dotStarRegex.search(primeObjective)
print('Print what .* finds in above string that will not include newlines')
print(matchObject.group())
print('')

dotStarAllRegex = re.compile(r'.*', re.DOTALL)
matchObject = dotStarAllRegex.search(primeObjective)
print('Print what .* plus re.DOTALL finds in above string with newlines')
print(matchObject.group())
print('')

#Force ignoring case with re.IGNORECASE
vowelRegex = re.compile(r'[aeiou]')
matchObject = vowelRegex.findall('What\'s with ROBOCOP?')
print('Printing just the lowercase vowel matches of "What\'s with ROBOCOP?"')
print(matchObject)

vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) #can also shorthand as re.I
matchObject = vowelRegex.findall('What\'s with ROBOCOP?')
print('Printing both the lowercase and uppercase vowel matches of "What\'s with ROBOCOP?"')
print(matchObject)
print('')

print('-----------------------------------------------------------')
print('Lesson 27. Regex Dot-Star and the Caret/Dollar Characters')
print('ENDS HERE')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')




print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson 28. Regex sub() Method and Verbose Mode')
print('STARTS HERE')
print('-----------------------------------------------------------')
print('')

agentNamesHere = 'Agent Alice gave the secret docs to Agent Scully'
print('String manipulated:')
print(agentNamesHere)
print('')

namesRegex = re.compile(r'Agent \w+')
matchObject = namesRegex.findall(agentNamesHere)
print('Agent names found in string:')
print(matchObject)
print('')

#Find and replace the agent names using the sub() method
matchObject = namesRegex.sub('***REDACTED***',agentNamesHere)
print('Agent names redacted from string using replacement by sub() method:')
print(matchObject)
print('')

#Use slash number syntax to use part of the target pattern match in output
namesRegex = re.compile(r'Agent (\w)\w*') #one word character in group followed by zero or more word characters
matchObject = namesRegex.findall(agentNamesHere)
print('Agent name first character found in string returned because it is captured in group 1:')
print(matchObject)
print('')
matchObject = namesRegex.sub(r'Agent \1******', agentNamesHere)
print('Using group 1 character to dynamically generate the text used in the sub() replacement text')
print(matchObject)
print('')

#Verbose regular expression strings -- Verbose Mode with re.VERBOSE

#use ''' to make complex regex object definition easier to read across multiple lines allowing for commenting
verboseText = re.compile(r'''
(\d\d\d-)|      #area code
(\(\d\d\d\)-)   #or area code with parentheses
\d\d\d          #first three digits
-               #second dash
\d\d\d\d        #last four digits
\sx\d{2,4}      #extension, like 1234''', re.VERBOSE | re.DOTALL | re.VERBOSE) #the Pipe here is the Bitwise Or Operator allowing adding more than one option in the second argument cummulatively

print('-----------------------------------------------------------')
print('Lesson 28. Regex sub() Method and Verbose Mode')
print('ENDS HERE')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson 29.  Regex Example Program: A Phone and Email Scraper')
print('STARTS HERE')
print('------------------------------------------------------------')
print('')

print('------------------------------------------------------------')
print('Lesson 29.  Regex Example Program: A Phone and Email Scraper')
print('ENDS HERE')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')

# Created new file instead

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Lesson XX. ...')
print('STARTS HERE')
print('-----------------------------------------------------------')
print('')

print('-----------------------------------------------------------')
print('Lesson XX. ...')
print('ENDS HERE')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')