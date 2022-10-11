
speed = int(input('Введите скорость: '))
time = int(input('Введите время: '))

point = speed * time 
if point > 109:
	print(point%109)
else:
	print(point)

