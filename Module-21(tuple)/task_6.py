# Задача 6. По парам
# Есть список из 10 случайных чисел. Напишите программу, которая делит эти числа на пары кортежей внутри списка, и выведите результат на экран.

# Дополнительно: решите задачу несколькими способами.

# Пример:

# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

lst =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_lst = []

cort =()
for i in range(len(lst)):
    if i % 2 == 0:
        new_lst.append((lst[i],lst[i +1]))
        cort += (lst[i],lst[i +1]),

cort = list(cort)
print(new_lst)
print(cort)