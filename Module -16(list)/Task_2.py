# Задача 2. Турнир
# Для соревнований по волейболу необходимо сформировать турнирнирную сетку для восьми человек на два дня. 
# На первый день решили выбрать каждого второго из списка участников.
# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар. 
# Напишите программу, которая выводит элементы списка только с чётными индексами.
# Пример:

# Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']


names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

day1 = []
day2 = []

for i in range(len(names)):
    if i % 2 == 0:
        day1.append(names[i])
    if i % 2 != 0:
        day2.append(names[i])

print('Первый день: ',day1)
print('Второй день : ',day2)



