import json

data = {}
def register():
	log = input('Enter your log: ')
	pswd = input('Create password: ')
	data[log] = pswd
	with open('data.json', 'w') as f:
		json.dump(data,f)
register()
def check()