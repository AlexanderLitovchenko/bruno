import time
from threading import Thread
def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

names = ['name1','tread','python','name4','last']
threads = [Thread(target = get_thread, args = (names[i], )) for i in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()