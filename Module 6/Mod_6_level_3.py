import requests
import time

def get_link(link):
	time.sleep(1)
	link = requests.get('https://github.com/AlexanderLitovchenko/new-repository')
	print(link)

links = ['https://www.youtube.com/','https://www.google.com/',
		'https://github.com/AlexanderLitovchenko/new-repository',
		'https://vk.com/feed', 'https://go.mail.ru/']

time1 = time.time()
for i in range(5):
	get_link(links[i])
time2 = time.time()
print('Время выполнения последовательного запуска: ', time2-time1)

from threading import Thread

threads = [Thread(target = get_link, args = (links[i], )) for i in range(5)]

time3 = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
time4 = time.time()
print('Время выполнения параллельного запуска: ', time4-time3)