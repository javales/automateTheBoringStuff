#! /usr/bin/env python3

# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 9: Running Programs from the Command Line (Lesson 22)

### 22. Launching Python Programs from Outside IDLE
###################################################

print('Hello Squirrels!')
print('')

#Windows Batch File Sample with %* at end to tell to forward command line arguments to code within py program called by batch file
# @py c:\users\al\mypythonscripts\hello.py %*

#Command line arguments/options are captured as a list of strings in sys.argv variable and can be accessed in code
import sys
print("Printing sys.argv strings of command line options entered")
print(sys.argv)
print("")