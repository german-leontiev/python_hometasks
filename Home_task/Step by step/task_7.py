print('Задача 7. Сумма ряда')
summ =0
n =int(input('Введите N: '))
for elem in range(0, n +1):
    elem = (-1)**n *1 /(2**n)
    summ += elem
print(elem)