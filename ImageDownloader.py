#! python3

import requests
import bs4
import webbrowser

res = requests.get('https://www.flickr.com/search/?q=dogs')
soup = bs4.BeautifulSoup(res.text, features="lxml")

#pictures = soup.select('main > div > div > div > div > div > div > div > a')
pictures = soup.findAll('div', class_="view photo-list-photo-view requiredToShowOnServer awake")
num = len(pictures)
print(num)

for i in range(num):
#    webbrowser.open('https://www.flickr.com/search/?q=dogs' + pictures[i].get('href'))
    print(pictures[i])
