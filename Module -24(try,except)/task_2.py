# Задача 2. Координаты
# Что нужно сделать
# Есть файл coordinates.txt, в котором хранится N пар из чисел X и Y. Оба числа передаются в первую функцию, 
# где к каждой координате прибавляется случайное число (от 0 до 5 и от 0 до 10) и возвращается результат деления X на Y. 
# Затем эти же координаты передаются во вторую функцию, где уже отнимается случайное число и возвращается Y/X.

# После этого формируется случайное число от 0 до 100, затем в файл result.txt в каждую строку записывается отсортированный список, 
# состоящий из этого случайного числа и двух полученных результатов.

# Один программист уже написал за нас программу для этой задачи, но «почему-то» его вариант решения отклонили. Вот его код:

# Отредактируйте и исправьте программу, убрав лишние вложенности try except.

# import random

 

# def f(x, y):

#     x += random.randint(0, 10)

#     y += random.randint(0, 5)

#     return x / y

 

# def f2(x, y):

#     x -= random.randint(0, 10)

#     y -= random.randint(0, 5)

#     return y / x

 

# try:

#     file = open('coordinates.txt', 'r')

#     for line in file:

#         nums_list = line.split()

#         res1 = f(int(nums_list[0]), int(nums_list[1]))

#         try:

#             res2 = f2(int(nums_list[0]), int(nums_list[1]))

#             try:

#                 number = random.randint(0, 100)

#                 file_2 = open('result.txt', 'w')

#                 my_list = sorted([res1, res2, number])

#                 file_2.write(' '.join(my_list))

#             except Exception:

#                 print("Что-то пошло не так : ")

#         except Exception:

#             print("Что-то пошло не так со второй функцией")

#         finally:

#             file.close()

#             file_2.close()

# except Exception:

#     print("Что-то пошло не так с первой функцией")



import random


def f(x, y):

    x += random.randint(0, 10)

    y += random.randint(0, 5)

    return x / y


def f2(x, y):

    x -= random.randint(0, 10)

    y -= random.randint(0, 5)

    return y / x

with open('coordinates.txt', 'w') as file: 
    file.write(str(random.randint(0,10))+ ' '+ str(random.randint(0,10))) 

with open('coordinates.txt', 'r') as file: 
    for line in file: 
        nums_list = line.split() 
        try: 
            res1 = f(int(nums_list[0]), int(nums_list[1])) 
        except Exception: 
            print("Что-то пошло не так с первой функцией") 
        try: 
            res2 = f2(int(nums_list[0]), int(nums_list[1])) 
        except Exception: 
            print("Что-то пошло не так со второй функцией") 

number = random.randint(0, 100) 
try: 
    with open('result.txt', 'w') as file_2: 
        my_list = sorted([res1, res2, number]) 
        file_2.write(' '.join(map(str, my_list))) 
except Exception: 
    print("Что-то пошло не так")



 

