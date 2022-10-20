class Model():
	
	def __init__(self):	
		self.title = '1'
		self.text = '2'
		self.author = '3'

	def save (self):
		import json
		b = Model()
		data = b.__dict__

		with open('allattr.json', 'w') as f:
			json.dump(data,f)

s = Model()
