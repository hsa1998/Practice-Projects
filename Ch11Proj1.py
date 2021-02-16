#! python3
import requests, sys, webbrowser, bs4


print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

txtdoc = open('txtdoc.txt', 'w')
txtdoc.write(res.text)

soup = bs4.BeautifulSoup(res.text, features="lxml")

linkElems = soup.select('div#main > div > div > div > a')
print(len(linkElems))
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
