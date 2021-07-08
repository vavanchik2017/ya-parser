import requests
import bs4
import re
import lxml

#url = "https://market.yandex.ru/catalog--smartfony-v-volzhskom/54726/list?cpa=0&hid=91491&track=pieces&onstock=1&page=5&local-offers-first=0"
pattern =  re.compile('/product--.*')
links = []
with open("index.html", "r") as file:
    content = file.read()
soup = bs4.BeautifulSoup(content,"lxml")
#sel = soup.select("div.d0N9PZYfeg a")
for titles in soup.findAll('a', href=True):
    a = re.findall(pattern, str(titles['href']))
    links.append(a)
templist = list(filter(None, links))

for x in templist:
    print (x)