# /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 14: Excel, Word, and PDF Documents (Lesson 42-45) - only Lesson 45 - Reading and Editing Word Documents

# Install third-party module with pip install python-docx to read and modify Word files

import docx

print('')
print('##############################################################################')
print('Section 14: Excel, Word, and PDF Documents (Lesson 42-45) - only Lesson 45 - Reading and Editing Word Documents')
print('##############################################################################')
print('')

# Lesson is for Word for Windows (not macOS)

# runs stop and start with new formatting of text

# all docx objects have a add_paragraph() method

# all paragraph objects have a add_run() method

# More Documentation: https://python-docx.1readthedocs.org