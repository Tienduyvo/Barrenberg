import requests
from bs4 import BeautifulSoup as bs

with requests.Session() as c:
    url = 'http://www.boerse.de/historische-kurse/wertpapier/DE000BASF111_jahr,2009#jahr'
    c.get(url)
    c.post(url, headers = {"Referer": "http://www.boerse.de"})
    page = c.get('http://www.boerse.de/historische-kurse/wertpapier/DE000BASF111_jahr,2009#jahr')
    soup = bs(page.content)
    prettyHTML = soup.prettify()
    price2009 = soup.findAll("td",{"class":"alignright"})
    print(price2009[169].text)