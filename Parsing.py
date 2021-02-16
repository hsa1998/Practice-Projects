import bs4
import requests as req
import re

URL = req.get('https://www.coingecko.com/en/coins/ethereum')
URLSoup = bs4.BeautifulSoup(URL.text, features="lxml")

elems = URLSoup.select('[data-coin-symbol="eth"][data-target="price.price"]')

x = (elems[0].getText())[1:]

price = float(re.sub(r'[$, ]', '', x))
print(price)
