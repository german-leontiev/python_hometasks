# Задача 4. Файлы и папки
# Что нужно сделать
# Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит общее количество файлов и подкаталогов в нём. 
# Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.

# Результат работы программы на примере python_basic\Module14:

# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кб): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15

import os




proj = ['Новая папка (3)']
for i in proj:
    path = os.path.abspath(os.path.join('..', i))


total_size = 0
file_count = 0
dir_count = 0

print('\nСодержимое директории:', path)


for root, dirs, files in os.walk(path):
    dir_count += len(dirs)
    for file in files:
        file_path = os.path.join(root, file)
        file_count += 1
        total_size += os.path.getsize(file_path)


print('Размер каталога (в Кб):', round(total_size / 1024))
print('Количество подкаталогов:', dir_count)
print('Количество файлов:', file_count)