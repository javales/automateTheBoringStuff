#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 16: GUI Automation (Lesson 48-51) - only Lesson 50 - Screenshots and Image Recognition

"""
Working with the Screen
Your GUI automation programs don’t have to click and type blindly. PyAutoGUI has screenshot features that can create an image file based on the current contents of the screen. These functions can also return a Pillow Image object of the current screen’s appearance. If you’ve been skipping around in this book, you’ll want to read Chapter 17 and install the pillow module before continuing with this section.

On Linux computers, the scrot program needs to be installed to use the screenshot functions in PyAutoGUI. In a Terminal window, run sudo apt-get install scrot to install this program. If you’re on Windows or OS X, skip this step and continue with the section.
"""

# install pillow module to access pillow screenshots
# for Linux, install scrot

import pyautogui

# The following screenshot() function returns a Pillow Image object
# call any method on this object as documented in Pillow documentation
print('Capturing screenshot and saving it as myFirstPillowScreenshot.png')
pyautogui.screenshot('myFirstPillowScreenshot.png')

# To do Image Recognition, use pyautogui.locateOnScreen(image to find on screen)
# "image to find on screen" is something like a button you cropped out of the calculator app

# THIS DOES NOT WORK
print('Print where the Safari dock icon is on screen')
print(pyautogui.locateOnScreen('clickSafari.png'))

# IF THE ABOVE WORKED, CAN MOVE TO CENTER OF IT USING:
x,y = pyautogui.locateCenterOnScreen('clickSafari.png')
pyautogui.moveTo((x,y), duration = 1)
pyautogui.click()

# This is all computationally expensive, so it takes about a second to find coordinates
# read pyautogui.readthedocs.org for info on how to speed up the matches

# sushigoroundbot on his github