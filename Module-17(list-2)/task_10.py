# Задача 10. Симметричная последовательность
# Что нужно сделать
# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево. 
# Например, следующие последовательности являются симметричными:

# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1

# Пользователь вводит последовательность из N чисел. 
# Напишите программу, которая определяет, какое минимальное количество и каких чисел надо добавить в конец этой последовательности, чтобы она стала симметричной.

# Пример 1:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2

# Последовательность: [1, 2, 1, 2, 2]
# Нужно добавить чисел: 3
# Сами числа: [1, 2, 1]

# Пример 2:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 3
# Число: 4
# Число: 5

# Последовательность: [1, 2, 3, 4, 5]
# Нужно добавить чисел: 4
# Сами числа: [4, 3, 2, 1]


number =int(input('Кол-во чисел: '))
num_list = []

for i in range(number):
    num =str(input('Число: '))
    num_list.append(num)


new_list =[]
count = 2

for i in range(1,len(num_list)):
    index = num_list[- count]
    count += 1
    new_list.append(index)



print('Последовательность: ',num_list)
print('Нужно добавить чисел: ',len(num_list)-1)
print('Сами числа: ', new_list)
num_list.extend(new_list)
print(num_list)