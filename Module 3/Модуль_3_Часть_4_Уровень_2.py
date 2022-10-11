import json

data = {}
def register():
	log = input('Enter your log: ')
	pswd = input('Create password: ')
	data[log] = pswd
	with open('data.json', 'w') as f:
		json.dump(data,f)
register()
def check():
	log = input('Enter your log: ')
	pswd = input('Create password: ')
	if log not in data.keys():
		data[log] = pswd
	else:
		print('user with this name already exists')
		register()
check()
