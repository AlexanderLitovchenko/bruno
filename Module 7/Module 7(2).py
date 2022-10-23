import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
info = soup.find('table',{'class':'mfd-table mfd-currency-table'}).find_all('td')

data = []
for item in info:
	data.append(item)

date = []
exchange_rate = []
for i in range(0,len(data),3):
	date.append(str(data[i].text[2:]))
	exchange_rate.append(float(str(data[i+1].text)))
date.reverse()
exchange_rate.reverse()



x = date
y = exchange_rate
figure, ax = plt.subplots()
ax.plot(x, y)
locator = MultipleLocator(25)
ax.xaxis.set_major_locator(locator)
ax.set(title='Курс доллара к рублю', xlabel='Дата', ylabel='Курс')
plt.grid()
plt.show()