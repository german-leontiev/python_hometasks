# Задача 9. Список списков
# Что нужно сделать
# Дан такой (уже многомерный!) список:

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список. 
# Для решения используйте только list comprehensions.

# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

very_nice_list =[ x for i in nice_list 
                    for a in i 
                    for x in a ]

print(very_nice_list)