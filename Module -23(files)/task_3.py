# Задача 3. Дзен Пайтона — 2
# Что нужно сделать
# Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt (который содержит всё тот же «Дзен Пайтона»). 
# Выведите три найденных числа на экран.

# Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.

# Формат вывода:
# Количество букв в файле:
# Количество слов в файле:
# Количество строк в файле:
# Наиболее редкая буква:
import os

text = 'abcdefghijklmnopqrstuvwxyz'
zen = open('zen.txt','r')
letter_count = 0
word_count = 0
str_count = 0
rare = {}
for i in zen.readlines():
    str_count += 1

for i in zen.read().split():
    word_count += 1

for i in zen.read():
    if i in text:
        letter_count += 1
    if i in rare:
        rare[i] += 1
    else:
        rare[i] = 1

print('Количество букв в файле: ',letter_count)
print('Количество слов в файле: ',word_count)
print('Количество строк в файле: ',str_count)
print('Наиболее редкая буква: ',min(rare,key=rare.get))
