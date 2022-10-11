def area():
    a = int(input('Введите значение 1: '))
    b = int(input('Введите значение 2: '))
    c = int(input('Введите значение 3: '))
    if a+b<c or a+c<b or b+c<a:
        print('Треугольника со сторонами',a,b,c,'не существует')
        area()
    else:
        p = (a+b+c)/2
        print((p*(p-a)*(p-b)*(p-c))**0.5)
area()