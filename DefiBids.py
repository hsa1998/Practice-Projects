#! python3

'''
1.      find a way to pull info from website and create a list of bid value to winning bid to
1.a)    find a way to track average bid count to determine
2.      run analysis on numbers to see if there is a prevailing bid value to winning bid ratio
'''

from selenium import webdriver
import time

path = 'C:\Drivers\chromedriver.exe'
url = 'https://auctions.defibids.com/lub/closed'

driver = webdriver.Chrome(path)
driver.get(url)

time.sleep(2)

body = driver.find_element_by_id("closedAuctions")
auctions = body.find_elements_by_class_name('auction-content')

for i in auctions:
    bid = i.find_element_by_class_name('amount bid')
    print(bid.text)
    value = i.find_element_by_class_name('amount-content')
    print(value.text)
#for i in section:
#    print(i.text)
#    if str(i.text) == 'Winning Bid':
#        print(i.text)
#    elif str(i.text) == 'Value':
#        print(i.text)
driver.quit()
