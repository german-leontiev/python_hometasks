# Задача 2. Генерация
# Что нужно сделать
# Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел. 
# На чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.

# Пример:

# Введите длину списка: 10

# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]

num =int(input('Введите длину списка: '))

num_list = [(i % 5 if i % 2 else 1) for i in range(num)]

print(num_list)