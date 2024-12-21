# Задача 6. Паранойя
# Что нужно сделать
# Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» с его компьютера, включая переписку с людьми. 
# Поэтому он эти переписки шифрует. И делает это с помощью шифра Цезаря (чем веселит агента службы безопасности).

# Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, 
# при этом символы первой строки файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее. 
# Результат выведите в файл cipher_text.txt.

# Пример

# Содержимое файла text.txt:

# Hello
# Hello
# Hello
# Hello

# Содержимое файла cipher_text.txt:

# Ifmmp
# Jgnnq
# Khoor
# Lipps

import os

lst = 'abcdefghijklmnopqrstuvwxyz'
lst_2 ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('text.txt', 'w') as file:
    for i in range(4):
        file.write('Hello\n')

with open('text.txt', 'r') as file:
    print('Содержимое файла text.txt: ')
    for i in file:
        print(i,end ='')

with open('text.txt', 'r') as file:
    count = 1
    cez = ''
    for i in file.read():
        if i in lst_2:
            place = lst_2.find(i)
            new_place = (place + count) % 26
            cez += lst_2[new_place]
        if i in lst:
            place = lst.find(i)
            new_place = (place + count) % 26
            cez += lst[new_place]
        if i == '\n':
            count += 1
            cez += '\n'


with open('cipher_text.txt', 'w') as cipher_text:
    cipher_text.write(cez)
with open('cipher_text.txt', 'r') as cipher_text:
    print('\nСодержимое файла cipher_text: ')
    for i in cipher_text:
        print(i,end ='')
