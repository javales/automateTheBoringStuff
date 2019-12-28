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