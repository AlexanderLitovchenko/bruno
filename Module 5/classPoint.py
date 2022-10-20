class Point():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__ (self,other):
		return Point(self.x + other.x, self.y + other.y)
	def distanse (self,other):
		return int(((self.x-other.x)**2+(self.y-other.y)**2)**0.5)

s = Point(5,7)
print(s.distanse)