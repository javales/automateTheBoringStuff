#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 16: GUI Automation (Lesson 48-51) - only Lesson 49 - Controlling the Keyboard from Python

import pyautogui

print(pyautogui.position())

pyautogui.click(-1491,609); pyautogui.typewrite('Hello Squirrels!')

# Instead of strings, can type keys or key sequences

pyautogui.typewrite(['a','b','left','left','right','x','y'],interval=.11)

# To get a list of the keys to type:
print('To get a list of the keys to type pyautogui.KEYBOARD_KEYS:')
print(pyautogui.KEYBOARD_KEYS)
print('')

# To press one ONE key use pyautogui.press()
pyautogui.press('F5')

# To do Windows Ctrl+O and such, use pyautogui.hotkey()
pyautogui.hotkey('ctrl','o')
