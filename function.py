import bs4
import re

pattern =  re.compile('/product--.*track=srchbtn.*')
links = []
with open("index.html", "r") as file:
    content = file.read()
soup = bs4.BeautifulSoup(content,"html.parser")
for titles in soup.findAll('a', href=True):
    a = re.findall(pattern, str(titles['href']))
    links.append(a)
templist = list(filter(None, links))
for x in templist:
    print(x)

