# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import bs4
import re
import sqlite3
from datetime import datetime

time = str(datetime.now().time())
name = "parse_"+time+".db"

db = open(name, "w+")

try:
    sqlite_connection = sqlite3.connect(name)
    sqlite_create_table_query = '''CREATE TABLE orders (
                                id INTEGER PRIMARY KEY,
                                links TEXT NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQL")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")
    sqlite_connection.commit()
    #cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


url = "https://market.yandex.ru/catalog--umnye-chasy-i-braslety/56034/list?hid=10498025"
pattern =  re.compile('/product--.*nid.*track=srchlink.*')

def parser(content):
	links = []
	templist=[]		
	f = open ('links.txt', 'w')
	soup = bs4.BeautifulSoup(content,"html.parser")
	for titles in soup.findAll('a', href=True):
		a = re.findall(pattern, str(titles['href']))
		links.append(a)
	templist = list(filter(None, links))
	for x in templist:
		cursor.execute("INSERT INTO orders (links) VALUES (?)",("market.yandex.ru"+x[0], ))
		sqlite_connection.commit()

	
driver = webdriver.Firefox()
driver.get(url)

try:
	element = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.LINK_TEXT, "Вперёд"))
	)

finally:
	while (driver.find_element_by_link_text('Вперёд')):
		try:
			html_source = driver.page_source
			parser(html_source)
			button = driver.find_element_by_link_text('Вперёд')
			button.click()
		except NoSuchElementException:
			html_source = driver.page_source
			parser(html_source)

cursor.close()

