import requests
import bs4
import re

#url = "https://market.yandex.ru/catalog--smartfony-v-volzhskom/54726/list?cpa=0&hid=91491&track=pieces&onstock=1&page=5&local-offers-first=0"
pattern =  re.compile('href="/product--')

with open("index.html", "r") as file:
    content = file.read()
soup = bs4.BeautifulSoup(content,"html.parser")
#sel = soup.select("div.d0N9PZYfeg a")
for titles in soup.findAll('a', href=True):
    print(titles['href'])
    #print(re.findall(pattern, str(titles)))