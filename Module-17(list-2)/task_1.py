# Задача 1. Страшный код
# Что нужно сделать
# Вашему другу, который тоже начал изучать Python, спикер дал следующие условия: есть три списка — основной и два побочных.
#  В основном лежат элементы [1, 5, 3], а в побочных — [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.

# Первый побочный закидывается в основной, в нём считается и выводится на экран количество цифр «5», а затем они удаляются из основного списка.
# После этого в основной закидывается второй побочный список, в нём считается и выводится на экран количество цифр «3». В конце также выводится и сам список.

# Из интереса вы попросили друга показать код его программы и поняли, что сделали это не зря, — то, что вы увидели, повергло вас в шок и ужас. Вот сам код:

# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# Используя знания о методах списков, а также о стиле программирования, помогите другу переписать программу. Не используйте дополнительные списки.

# Результат работы программы:

# Кол-во цифр 5 при первом объединении: 3

# Кол-во цифр 3 при втором объединении: 4

# Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]



main = [1, 5, 3]
second = [1, 5, 1, 5]
second_2 = [1, 3, 1, 5, 3, 3]

count = 0
count_2 = 0
new_list = []

for i in second:
    main.append(i)
for i in main:
    if i == 5:
        count += 1



for i in main:
    if i != 5:
        new_list.append(i)
for i in second_2:
    new_list.append(i)
for i in new_list:
    if i == 3:
        count_2 += 1

print('Кол-во цифр 5 при втором объединении: ', count)        
print('Кол-во цифр 3 при первом объединении: ', count_2)
print('Итоговый список: ', new_list)