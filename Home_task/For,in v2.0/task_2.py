print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
num =int(input('Введите число: '))
for a in range(num +1):
    for b in range(a):
        print(a,end =' ')
    print()