import requests
from bs4 import BeautifulSoup


page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
info = soup.find('table',{'class':'mfd-table mfd-currency-table'}).text
print(info)
