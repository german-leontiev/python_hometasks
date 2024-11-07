print('Задача 6. Спецшифр')

text =input('Введите строку: ')
s = 0
count = 0

for symbol in text:
    if symbol == 's' or symbol == 'S':
        count += 1
    elif count > s:
        s = count
        count = 0
print('Самая длинная последовательность: ',s)
#Хз что надо,но он считает ТОЛЬКО если после 'S' есть другая буква



