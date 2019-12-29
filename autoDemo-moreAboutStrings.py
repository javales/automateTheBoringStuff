# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 8: More About Strings (19 - 21_

### 19. Advanced String Syntax
##############################

#Escape Characters
saywhat = "That is Alice's cat"
print(saywhat)
print("")

print('Hello there!\nHow are you?\nI\'m fine.')
print("")

#Raw Strings useful when have a lot of backslashes
print(r'That is Carol\'s cat.')
print("")

#Multi-line String
print("""Dear Alice,
Eve's cat has been found safe,
Yay, let's celebrate.
- Jim""")
print("")

spam = """Dear Alice,
Eve's cat has been found safe,
Yay, let's celebrate.
- Jim"""
print(spam)
print("")

spam = 'Hello world!'
print(spam)
print("")

#Strings can be treated like lists with list items
print("First index of phrase")
print(spam[0])
print("")

#and sliced
print("Print slice range of phrase")
print(spam[1:5])
print("")

#negative index
print("Print negative first index of phrase")
print(spam[-1])
print("")

#in and not in
print("Hello in spam?")
print('Hello' in spam)
print("")

print("nada in spam?")
print('nada' in spam)
print("")

### 20. String Methods
######################

print("Enter some form of the word \"Yes\"")
answer = raw_input() ##input()##DOES##NOT##WORK##IN##2.7.16##
print("You entered:")
print(answer)
print("")

if answer == "yes":
    print("Since you entered \"yes\"")
    print('Playing, again')
    print("")

print("Enter some form of the word \"Yes\"")
answer = raw_input() ##input()##DOES##NOT##WORK##IN##2.7.16##
print("You entered:")
print(answer)
print("")

if answer == 'YES':
    print("Since you entered \"YES\"")
    print('Playing, again')
    print("")

print("Enter some form of the word \"Yes\"")
answer = raw_input() ##input()##DOES##NOT##WORK##IN##2.7.16##
print("You entered:")
print(answer)
print("")

if answer.lower() == 'yes':
    print("You entered some form \"YeS\"")
    print("")

#Check if all characters lowercase or uppercase
print(answer.islower())
print(answer.isupper())
#    print("islower() confirms all lower case")

print("Print answer in uppercase")
print(answer.upper())

print("Print answer to appear to be now uppercase")
print("Using isupper() method")
print(answer.upper().isupper())

"Print confirmation answer is immutable"
print("Print answer")
print(answer)

print("")

#other methods: isalpha, isalnum, isdecimal, isspace, istitle, title, startswith, endswith

#join strings with a specified string in between
print("Joining three strings with the , string using join()")
print(','.join(['cats','rats','bats']))
print('')

#split a string up into multiple strings based on string pattern
print('My name is Simon.'.split('m'))
print('')

#use ljust and rjust to add whitespace padding to left or right to meet length specified
print("Hello right-justified to 10")
print('Hello'.rjust(10))
print('')
print("Hello left-justified to 10")
print('Hello'.ljust(10))
print('')

#use ljust and rjust to add specified padding to left or right to meet length specified
print("Hello right-justified to 10")
print('Hello'.rjust(10,'*'))
print('')
print("Hello left-justified to 10")
print('Hello'.ljust(10,'*'))
print('')

#use center to center within length specified and pad with whitespace or specified character
print('Yellow centered to 20')
print('Yellow'.center(20))
print('Yellow'.center(20,'+'))
print('')

#strip, lstrip, and rstrip remove whitespace from ends of string
#can also specify what string to remove from ends of string
print('Using one of the strip methods to strip out letters of spam from ends')
print('SpammusteatsSpam'.strip('ampS'))
print('')

#replace one string pattern with another within a string
print('Using replace method to replace e with 3')
print('Hello there'.replace('e','3'))
print('')

#import pyperclip to use its copy() and paste() functions to access the clipboard 15:52


### 21. String Formatting
#########################

#Conversion specifiers
name = 'Alice'
place = 'Main Street'
time = '6pm'
food = 'turnips'

print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name,place,time,food))

#BASIC MATERIAL COMPLETE!