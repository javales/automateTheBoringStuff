#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 10: Regular Expressions (Lesson 29)

### 29. Regex Example Program: A Phone and Email Scraper
########################################################

import re, pyperclip, pprint

# TODO: Create a regex object for phone numbers
phoneRegex = re.compile(r'''
# 415-555-9999, 444-333, (415) 443-3333, 333-3333 ext 12345, ext. 12345, x12354

(
((\d\d\d) | (\(\d\d\d\)))?  #area code (optional)
(\s|-)                      #first separator
\d\d\d                      #first 3 digits
-                           #separator
\d\d\d\d                    #last 4 digits
(((ext(\.)?\s)|x)           #extension(optional)
(\d{2,5}))?                 #extension continued (optional)
)                           #since there are MULTIPLE groups, combine all into one group ??? but don't undertand why ???
                            #output showed the first string in each tuple as the phone number
''', re.VERBOSE)

# TODO: Create a regex object for email addresses
emailRegex = re.compile(r'''
# some.+_thing@some.+_thing.com
[a-zA-Z0-9_.+]+             # name part character class where you don't have to escape out certain characters
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part

''', re.VERBOSE)


# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
phoneRegex.findall(text)

# TODO: Copy the extracted email/phone to clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print('Extracted Phone')
pprint.pprint(allPhoneNumbers)
print('Extracted Email')
pprint.pprint(extractedEmail)
print('')

results = '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmail)
print(results)
pyperclip.copy(results)