# Задача 3. Клетки
# Что нужно сделать
# В научной лаборатории выводят и тестируют новые виды клеток. 
# Есть список из N этих клеток, элементом которого является показатель эффективности, а индексом — ранг клетки. 
# Учёные отбирают клетки по следующему принципу — если эффективность клетки меньше её ранга, то она не подходит.

# Напишите программу, которая выводит на экран элементы списка, значения которых меньше их индекса.

# Пример:

# Количество клеток: 5
# Эффективность 1 клетки: 3
# Эффективность 2 клетки: 0
# Эффективность 3 клетки: 6
# Эффективность 4 клетки: 2
# Эффективность 5 клетки: 10
# Неподходящие значения: 0 2



num =int(input('Количество клеток: '))
bad_bio = []
bio = []

for i in range(num):
    bio_num =int(input(f'Эффективность {i + 1} клетки: '))
    if bio_num < i:
        bad_bio.append(bio_num)
    else:
        bio.append(bio_num)

print('Неподходящие значения: ',bad_bio)
print('Подходящие значения: ', bio)