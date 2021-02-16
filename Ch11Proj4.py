#! python3
'''
1. go to a photo-sharing website
2. searches for a picture, maybe will be user inputted
3. downloads all the images
bonus. make it so that it works with any website
'''

import sys
from selenium import webdriver
import time
import bs4
import requests

search = 'dogs'
#search = ' '.join(sys.argv[1:])

browser = webdriver.Chrome('C:\\Drivers\\chromedriver')
browser.get('https://www.flickr.com/creativecommons')

browser.find_element_by_id('truste-consent-required').click()
searchBar = browser.find_element_by_id('gn-search-field')
searchBar.send_keys(search)
searchBar.submit()

soup = bs4.BeautifulSoup(requests.get(browser.current_url).text, features='lxml')

pictures = soup.select('a[role="heading"]')
print(len(pictures))

#for i in pictures[0]:
#    i.click()
#    browser.find_element_by_class_name('ui-icon-download').click()
#    browser.find_element_by_class_name('download-image-size')
