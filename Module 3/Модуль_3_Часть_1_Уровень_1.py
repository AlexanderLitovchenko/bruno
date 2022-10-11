x =   int(input('Введите размер вклада: '))
p =   int(input('Введите количество процентов: '))
y =   int(input('Введите размер желаемого вклада: '))
       #x*(p/100) = 10 к вкладу за год

year = 0
year_list = []

while x <= y: 
	
	x = x + x*(p/100)
	year += 1
	year_list.append(year)
	
print('Через',year_list[-1],'лет размер вклада будет',y)	
