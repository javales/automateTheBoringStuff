#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 16: GUI Automation (Lesson 48-51) - only Lesson 48 - Controlling the Mouse from Python

"""
Shutting Down Everything by Logging Out
Perhaps the simplest way to stop an out-of-control GUI automation program is to log out, which will shut down all running programs. On Windows and Linux, the logout hotkey is CTRL-ALT-DEL. On OS X, it is -SHIFT-OPTION-Q. By logging out, you’ll lose any unsaved work, but at least you won’t have to wait for a full reboot of the computer.

Pauses and Fail-Safes
You can tell your script to wait after every function call, giving you a short window to take control of the mouse and keyboard if something goes wrong. To do this, set the pyautogui.PAUSE variable to the number of seconds you want it to pause. For example, after setting pyautogui.PAUSE = 1.5, every PyAutoGUI function call will wait one and a half seconds after performing its action. Non-PyAutoGUI instructions will not have this pause.

PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui.FailSafeException exception. Your program can either handle this exception with try and except statements or let the exception crash your program. Either way, the fail-safe feature will stop the program if you quickly move the mouse as far up and left as you can. You can disable this feature by setting pyautogui.FAILSAFE = False. Enter the following into the interactive shell:


>>> import pyautogui
>>> pyautogui.PAUSE = 1
>>> pyautogui.FAILSAFE = True
Here we import pyautogui and set pyautogui.PAUSE to 1 for a one-second pause after each function call. We set pyautogui.FAILSAFE to True to enable the fail-safe feature.
"""

# Directly controlling mouse and keyboard using pyautogui module using import pyautogui
# pip install pyautogui
# https://pyautogui.readthedocs.org

# 0,0 coordinate increases x to right and y down

import pyautogui

print('##############################################################################')
print('# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview')
print('## Section 16: GUI Automation (Lesson 48-51) - only Lesson 48 - Controlling the Mouse from Python')
print('')
yoScreenSizeIs = pyautogui.size()
print('Your Screen Size Resolution is:')
print(yoScreenSizeIs)
print('')

# Use multiple assignment to capture output of size()
width, height = pyautogui.size()
print('Width is captured in width variable')
print(width)
print('Height is captured in height variable')
print(height)
print('')

# Return the current coordinates of the mouse cursor with pyautogui.position()
x, y = pyautogui.position()
print('X coordinate is captured in x variable')
print(x)
print('Y is captured in y variable')
print(y)
print('')

# Move to a certain position using pyautogui.moveTo()
print('Send the pointer to (10,10)')
print('')
pyautogui.moveTo(10,10)
print('Now over to (100,100) to prepare for the slo mo... :)')
print('')
pyautogui.moveTo(100,100)

# Move, but show travel to position using duration argument
print('Send the pointer to (10,10), but show me...')
print('')
pyautogui.moveTo(10,10, duration=1.75)

# Move relative to current position, but show travel to position using duration argument
print('Send the pointer to (150,150), but show me...')
print('')
pyautogui.moveTo(150,150, duration=1.75)

# Click on a mouse position using pyautogui.click()
print('Clicking on PyCharm\'s Help menu')
print('')
pyautogui.click(-1218,-342) #alternatively can doubleClick, rightClick, middleClick,...

# Aside from moveTo and moveRel, there is dragRel and dragTo
# see cool demo using a gradual reduction of a moveDistance variable "distance"

# Can see coordinates in real-time in Windows example running the following at command prompt:
# pyautogui.displayMousePosition()
# sample output showing color in the tuple: X: 203 Y: 52 RGB: (199, 200, 201)