# Задача 1. Имена — 2
# Что нужно сделать
# Есть файл people.txt, в котором построчно хранится N имён пользователей.

# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму. 
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой именно строке возникла ошибка. 
# Программа при этом не завершается и обрабатывает все имена файла.

# Также при желании можно вывести все ошибки в отдельный файл errors.log.

# Пример работы программы

# Содержимое файла people.txt:

# Василий
# Николай
# Надежда
# Никита
# Ян
# Ольга
# Евгения
# Кристина

# Ответ в консоли:

# Ошибка: менее трёх символов в строке 5.
# Общее количество символов: 49.

with open('people.txt', 'w') as people:
    people.write('Василий\n')
    people.write('Николай\n')
    people.write('Надежда\n')
    people.write('Никита\n')
    people.write('Ян\n')
    people.write('Ольга\n')
    people.write('Евгения\n')
    people.write('Кристина')
    # Для тебя сделал,если проверять будешь работоспособность,чтоб файл создался)



with open('people.txt', 'r') as people:
    count = 0
    summ = 0
    error = ''
    for i in people:
        print(i, end='')
        length = len(i.strip())
        summ += length
        count += 1  #Аааааа
        try:
            if length < 3:
                raise ValueError
        except ValueError:
            error += f'Ошибка: менее трёх символов в строке {count}'




print(f'\n\nОбщее количество символов {summ}')
print(error)
