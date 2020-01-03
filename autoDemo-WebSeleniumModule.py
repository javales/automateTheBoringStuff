#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 13: Web Scraping (Lesson 38-41) - only Lesson 41 - Controlling the Browser with the Selenium Module

# sometimes sites require login or reacting to JavaScript
#
# Use Selenium to launch a browser that it can progrmattically control
# call functions to find html in browser, forms or login fields to fill, and click Submit buttons
# must install it as a third-party module pip install selenium
# import it as "from selenium import webdriver"
# ALSO download and put geckodriver for Firefox in this path: /Proj/study/udemy/automateTheBoringStuff/venv/bin
# use echo $PATH to confirm what path is appropriate

from selenium import webdriver
import time

# Launch Firefox
browser = webdriver.Firefox()
# browser2 = webdriver.Safari() # does not work due to error: "selenium.common.exceptions.SessionNotCreatedException: Message: Could not create a session: You must enable the 'Allow Remote Automation' option in Safari's Develop menu to control Safari via WebDriver."

# Tell Firefox where to go
browser.get('https://adafruit.com')

# Tell Firefox what to click (the Adabox navigation bar link up top)
# find FIRST matching element
##site-header > div > ol > li:nth-child(6) > a
element = browser.find_element_by_css_selector('#site-header > div > ol > li:nth-child(6) > a')
# can also find multiple elements using plural form browser.find_elements_by_css_selector

# Tell Firefox to click it
element.click()

# Find the search bar, type in it, submit
# This was not actually the CSS selector:
# <input id="search" type="text" name="q" autocomplete="off" data-page="" ,="" data-app-id="W9DMM4OTH0" data-app-key="e613bcda3453b9ef887e2724362f9e57" data-app-index="learn_guides_production" data-app-uri="https://learn.adafruit.com">

searchElement = browser.find_element_by_css_selector('#search')
searchElement.send_keys('xmas')
searchElement.submit() #automated, saves us trouble of finding what to click! YAY!
time.sleep(2)

# Miscellaneous
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.refresh()
time.sleep(2)
browser.quit()

# Reading Content
# #inner-wrapper > div:nth-child(5) > div > div > div:nth-child(2) > div.col-lg-8.col-md-8.col-sm-6.col-xs-12 > div.adabox-header

browser = webdriver.Firefox()
browser.get('https://adafruit.com')
element = browser.find_element_by_css_selector('#site-header > div > ol > li:nth-child(6) > a')
element.click()
textElement = browser.find_element_by_css_selector('#inner-wrapper > div:nth-child(5) > div > div > div:nth-child(2) > div.col-lg-8.col-md-8.col-sm-6.col-xs-12 > div.adabox-header')
textOfElement = textElement.text
print('Printing text of element found:')
print(textOfElement)
print('')
browser.quit()

# For entire text of website, use html or body element
browser = webdriver.Firefox()
browser.get('https://adafruit.com')
element = browser.find_element_by_css_selector('html')
textOfElement = element.text
print('Printing text of element found:')
print(textOfElement)
print('')
browser.quit()

# More Selenium documentation: https://selenium-python.readthedocs.org