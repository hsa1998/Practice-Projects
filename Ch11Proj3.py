#! python3
# Usage: call program with email address as arg1 and string as arg2:
'''
1. take inputs from the command line using sys
2. from selenium import webdriver to log into email address
3. using selenium to write up an email to user with string, both which will be provided in sys.argv
'''


import sys
from selenium import webdriver

receiver = sys.argv[1]
message = ' '.join(sys.argv[2:])

email = 'afridihaseeb98@gmail.com'
password = 'Haseeb98'

browser = webdriver.Chrome('C:\\Drivers\\chromedriver')
browser.get('http://mail.google.com')

usernameInput = browser.find_element_by_id('identifierId')
usernameInput.send_keys(email)

button = browser.find_elements_by_tag_name('button')
button[2].click()

passwordInput = browser.find_element_by_name('password')
passwordInput.send_keys(password)

browser.find_element_by_tag_name('button').click()

browser.find_element_by_class_name('T-I T-I-KE L3').click()

browser.find_element_by_id(':18v').send_keys(receiver)
browser.find_element_by_id(':19i').send_keys(message)
browser.find_element_by_id(':183').click()

