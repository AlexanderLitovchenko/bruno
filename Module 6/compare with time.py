import time

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

names = ['name1','tread','python','name4','last']
time1 = time.time()
for i in range(5):
	get_thread(names[i])
time2 = time.time()

print('Время выполнения программы: ',time2-time1)

import time
from threading import Thread
def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

names = ['name1','tread','python','name4','last']
threads = [Thread(target = get_thread, args = (names[i], )) for i in range(5)]

time1 = time.time()
for t in threads:
	t.start()

for t in threads:
	t.join()
time2 = time.time()

print('Время выполнения программы: ',time2-time1)