# Задача 1. Сумма чисел — 2
# Что нужно сделать
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк.
# Напишите программу, которая выводит сумму чисел в выходной файл answer.txt.

# Пример

 

# Содержимое файла numbers.txt

#      2
 
# 2
#   2
#          2

# Содержимое файла answer.txt

# 8

import os

with open('numbers.txt','r') as num:
    count= []
    print('Содержимое файла numbers.txt')
    for i in num:
        print(i, end=' ')
        for n in i.split():
            count.append(int(n))

    answer =sum(count)


with open('answer.txt','w') as new_num:
    new_num.write(str(answer))
    print('\nСодержимое файла answer.txt','\n',answer)





