# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 7: Dictionaries
### 17. The Dictionary Data Type

# Pretty Print Module
import pprint

# In dictionaries, indexes are keys
message = 'It was bright cold day in April, and the clocks were striking thirteen.'
# Can use triple quote ''' to auto-escape everything including going over multiple lines like in a paragraph

# Dictionary starting off empty, with no keys
count = {}

# A string is a list-like value, so you can use it in a for loop
for character in message.upper(): # use upper method so letter A is only counted once
    # Setting count dictionary to start off with zero value upon starting the count
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# Dictionaries have no order to them, so the output is random
print(count)

# Pretty Print (import first)
pprint.pprint(count)
captureText = pprint.pformat(count) # Capturing pprint output as a string with pformat function
print("Printing pformat capture of captureText variable")
print(captureText)