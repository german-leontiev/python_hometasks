# Задача 4. Регистрация
# Что нужно сделать
# У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt. 
# Каждая строка содержит имя, имейл и возраст, разделённые пробелами. Например: Василий test@test.ru 27.

# Напишите программу, которая проверяет данные из файла для каждой строки:

# Присутствуют все три поля.
# Поле «Имя» содержит только буквы.
# Поле «Имейл» содержит @ и . (точку).
# Поле «Возраст» является числом от 10 до 99.
# В результате проверки сформируйте два файла:

# log — для правильных данных, записывать строки в том виде, как есть;
# log — для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:

# НЕ присутствуют все три поля: IndexError.
# Поле «Имя» содержит НЕ только буквы: NameError.
# Поле «Имейл» НЕ содержит @ и . (точку): SyntaxError.
# Поле «Возраст» НЕ является числом от 10 до 99: ValueError.
# Формат выходных данных

# Содержимое файла registrations_bad.log:

# Ольга kmrn@gmail.com 123            Поле «Возраст» НЕ является числом от 10 до 99
# Чехова kb@gmail.com 142              Поле «Возраст» НЕ является числом от 10 до 99
# ……
# Степан ky 59             Поле «Имейл» НЕ содержит @ и . (точку)
# ……

# Содержимое файла registrations_good.log:
# Геннадий ttdababmt@gmail.com 69
# Ольга ysbxur@gmail.com 20
# ……

import string


def main(name, mail, age):
    try:
        if not name.isalpha():
            raise NameError(".................Поле «Имя» содержит НЕ только буквы")
        if '@' not in mail or '.' not in mail:
            raise SyntaxError(".................Поле «Имейл» НЕ содержит @ и . (точку)")
        if  int(age) >= 99 or int(age) <= 10:
            raise ValueError(".................Поле «Возраст» НЕ является числом от 10 до 99")
    except ValueError as e:
        raise ValueError(".................Поле «Возраст» НЕ является числом от 10 до 99") from e
    except (NameError, SyntaxError) as e:
        raise e

def process_registration(line, good_log, bad_log):
    try:
        name, mail, age =line.strip().split()
        main(name, mail, age)
        good_log.write(f"{name}{mail}{age}\n")
    except (IndexError, NameError, SyntaxError, ValueError) as e:
        bad_log.write(f"{line.strip()}{str(e)}\n")


with open('registrations.txt', 'r') as file, \
         open('registrations_good.log', 'w') as good_log, \
         open('registrations_bad.log', 'w') as bad_log:
        for line in file:
            process_registration(line, good_log, bad_log)


with open('registrations_bad.log', 'r') as bad_log:
    print('Содержимое файла registrations_bad.log:\n ')
    for i in bad_log:
        print(i,end ='')
with open('registrations_good.log', 'r') as good_log:
    print('Содержимое файла registrations_good.log:\n ')
    for i in good_log:
        print(i,end ='')