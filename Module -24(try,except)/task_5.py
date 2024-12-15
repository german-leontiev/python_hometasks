# Задача 5. Текстовый калькулятор
# Что нужно сделать
# Иван стоит на пороге величайшего открытия (не будем его расстраивать), которое перевернёт представление обо всей математике и программировании. 
# Имя этому открытию — текстовый калькулятор. Правда, код для своего открытия ему сложно написать самому, и поэтому он попросил вас помочь ему. 
# Так что уже можно бежать в патентное бюро.

# Есть файл calc.txt, в котором хранятся записи вида:

# 100 + 34,
# 23 / 4,
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделённые пробелами.

# Операнды — целые числа. Операции — арифметические (включая деление нацело и нахождение остатка).

# Напишите программу, которая вычисляет все эти операции и находит сумму их результатов. Пропишите обработку возможных ошибок. 
# Программа не должна завершаться при первой же ошибке, она учитывает все верные строки и выводит найденный ответ.

# После успешного выполнения задания, попробуйте модифицировать задачу. 
# Теперь пользователю на экран должно выводиться сообщение с ошибочной строкой и предложением её исправить.

# Пример 1

# Содержимое файла calc.txt:

# 100 + 34
# 10 +* 3
# 23 / 4

# Содержимое консоли:

# Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? Да

# Введите исправленную строку: 10 + 3

# Сумма результатов: 152.75

# Пример 2

# Содержимое файла calc.txt:

# 100 + 34
# 10 +* 3
# 20 -* 2
# 23 / 4

# Содержимое консоли:

# Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? Нет
# Обнаружена ошибка в строке: 20 -* 2   Хотите исправить? Да
# Введите исправленную строку: 20 - 2
# Сумма результатов: 157.75

with open('calc.txt','w') as file:
    file.write('100 + 34\n')
    file.write('10 +* 3\n')
    file.write('20 -* 2\n')
    file.write('23 / 4')


result =[]
with open('calc.txt', 'r') as file:
    for i in file.readlines():
        try:
            result.append(eval(i)) #А так можно? Именно для этой задачи можно,но лучше не над?
        except:
            q =input((f'Обнаружена ошибка в строке: {i} Хотите исправить? '))
            if q.lower() == 'да':
                line = input('Введите исправленную строку:')
                result.append(eval(line))
print('Сумма результатов: ',sum(result))

