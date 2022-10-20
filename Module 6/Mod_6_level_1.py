import time

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

names = ['name1','tread','python','name4','last']
time1 = time.time()
for i in range(5):
	get_thread(names[i])
time2 = time.time()
print(time2-time1)