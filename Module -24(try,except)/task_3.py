# Задача 3. Счастливое число
# Что нужно сделать
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма этих чисел не станет больше либо равна 777. 
# Каждое введённое число при этом дозаписывается в файл out_file.txt. 
# Сделайте так, чтобы перед дозаписью программа с вероятностью 1 к 13 выбрасывала пользователю случайное исключение и завершалась.

# Пример 1

# Введите число: 10
# Введите число: 500
# Введите число: 200
# Введите число: 67
# Вы успешно выполнили условие для выхода из порочного цикла!

# Содержимое файла out_file.txt:

# 10
# 500
# 200
# 67

# Пример 2

# Введите число: 10
# Введите число: 500
# Вас постигла неудача!

# Содержимое файла out_file.txt:

# 10

import random

with open('out_file.txt','w') as file:
    count = 0
    while True:
            lose = random.randint(1,13)
            num =int(input('Введите число: '))
            count += num
            file.write(str(num) + '\n')
            if lose == 5:
                print('Вас постигла неудача!')
                file.write('Вас постигла неудача!')
                break
            if count >= 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                file.write('Вы успешно выполнили условие для выхода из порочного цикла!')
                break

print('\nСодержимое файла out_file.txt:')
with open('out_file.txt','r') as file:
    for i in file:
        print(i,end ='')
