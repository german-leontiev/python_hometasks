print('Задача 3. Аналог Steam')

# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление, для пользователя необходимо отображать количество скачанных процентов,
# чтобы он понимал, успеет ли заварить чай, прежде чем завершится процесс.
# Каждое обновление игры требует разного количества мегабайтов, при этом у разных игроков разная скорость интернет-соединения.

# Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость интернет-соединения в мегабайтах в секунду.
# Для каждой секунды программа должна рассчитывать и выводить на экран процент скачанного объёма до тех пор, пока скачивание не завершится.
# В конце программа должна показать, сколько секунд заняло скачивание обновления. Обеспечьте контроль ввода.

# Пример
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения: 27
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

import math


second = 1
file =int(float(input('Укажите размер файла для скачивания: ')))
speed =int(float(input('Какова скорость вашего соединения: ')))
filemb = 0
for filemb in range(speed, file, speed):
        print('Прошло', second, 'сек. Скачано', filemb, 'из', file, 'Мб', math.ceil(100 * filemb / file),'%')
        second += 1
else:
    print('Прошло', second, 'сек. Скачано', file, 'из', file, 'Мб', math.ceil(100 * file / file),'%')