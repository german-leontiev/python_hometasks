# Задача 8. Частотный анализ
# Что нужно сделать
# Есть файл text.txt, который содержит текст. 
# Напишите программу, которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте, 
# и выводит результат в файл analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно.

# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. 
# Буквы должны быть отсортированы по убыванию их доли. 
# Буквы с равной долей должны следовать в алфавитном порядке.

# Пример

# Содержимое файла text.txt:

# Mama myla ramu.

# Содержимое файла analysis.txt:

# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083


import string


with open('text.txt', 'w') as text:
    text.write(input('Введите что-нибудь: '))


with open('text.txt', 'r') as text:
    print('Содержимое файла text.txt: ')
    for i in text:
        print(i, end='')


with open('text.txt', 'r') as text:
    a = {}
    count = 0
    for i in text.read():
        if i.lower() in string.ascii_lowercase: #Спс ИИ
            if i.lower() in a:
                a[i.lower()] += 1
            else:
                a[i.lower()] = 1
            count += 1

for i in a:
    a[i] = round(a[i] / count, 3)


b = sorted(a.items(), key=lambda x: (-x[1], x[0]))


with open('analysis.txt', 'w') as anal:
    for i, v in b:
        anal.write(f'{i} {round(v,3)}\n')


with open('analysis.txt', 'r') as anal:
    print('\nСодержимое файла analysis.txt:')
    for i in anal:
        print(i, end='')