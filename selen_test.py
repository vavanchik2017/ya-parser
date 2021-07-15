from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
import re

url = "https://market.yandex.ru/catalog--umnye-chasy-i-braslety/56034/list?hid=10498025"
pattern =  re.compile('/product--.*nid.*track=srchlink.*')
links = []

def parser(content):
	f = open ('links.txt', 'w')
	soup = bs4.BeautifulSoup(content,"html.parser")
	for titles in soup.findAll('a', href=True):
		a = re.findall(pattern, str(titles['href']))
		links.append(a)
	templist = list(filter(None, links))
	f.writelines(["%s\n" % x for x in templist])

driver = webdriver.Firefox()
driver.get(url)
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Вперёд"))
    )
finally:
	while (driver.find_element_by_link_text('Вперёд')):
			html_source = driver.page_source
			parser(html_source)
			button = driver.find_element_by_link_text('Вперёд')
			button.click()
