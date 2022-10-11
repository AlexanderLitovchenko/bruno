num = int(input('Введите целое число: '))
summ = 0
while num!=0:
	k = num%10
	summ = summ + k
	num = num//10
print(summ)
    