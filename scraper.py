import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
page = urlopen(url)
soup = bs4.BeautifulSoup(page,"html.parser")

def parsePrice():
 page = urlopen(url)
 price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
 return price
while True:
 print(parsePrice())

