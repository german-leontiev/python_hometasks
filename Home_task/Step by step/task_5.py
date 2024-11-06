print('Задача 5. Функция')
start =int(input('Введите начало отрезка: '))
stop =int(input('Введите конец отрезка: '))
step =int(input('Введите шаг: '))
for cut in range(stop, start -1, step):
    Function = (cut **3) + (2* cut**2) - (4 * cut) + 1
    print('В точке', cut , 'функция равна: ', Function)
