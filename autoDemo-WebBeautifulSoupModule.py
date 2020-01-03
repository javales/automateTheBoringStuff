#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 13: Web Scraping (Lesson 38-41) - only Lesson 40 - Parsing HTML with the Beautiful Soup Module

# Real Web Scraping Begins, Now!
# inspect element on specific area of webpage

# Use Beautiful to easily parse HTML for the specific area of interest
# must install it as a third-party module pip install beautifulsoup4
# import it as bs4

import bs4, requests

# https://www.adafruit.com/product/2441

# Use Beautiful Soup to find price element
def getAdafruitPiTFTPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    # capture resource text in Beautiful Soup variable, using bs function and specify html.parser (to avoid info message saying it was used by default)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # select all elements in specified css path
    soupFoundPriceElements = soup.select('#inner-wrapper > div.main-container.container > div.row.product-info > div.mobile-product-header > div.product-price > span') #pass in the string of the css selector

    # get the single element out to find the price and get its text attribute
    return soupFoundPriceElements[0].text #if element is heavily padded with newlines and spaces, use elems[0].text.strip()

# Call function with product's URL
soupFoundPrice = getAdafruitPiTFTPrice('https://www.adafruit.com/product/2441')

# Print Result:
print('##############################################################################')
print('# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview')
print('## Section 13: Web Scraping (Lesson 38-41) - only Lesson 40 - Parsing HTML with the Beautiful Soup Module')
print('')
print('Price of PiTFT, today:')
print(soupFoundPrice)
print('')