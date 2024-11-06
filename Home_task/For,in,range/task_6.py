print('Факториал')
num = 1
n = int(input('Введите натуральное число: '))
for c in range(1,n +1):
    num *= c
print('Факториал числа ', n, 'равен ', num)