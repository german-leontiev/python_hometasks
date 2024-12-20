# Задача 8. Бегущая строка
# Что нужно сделать
# В одной из практических работ вы писали для табло программу, которая циклически сдвигает элементы списка чисел вправо на K позиций. 
# В этот раз вы работаете с двумя строками. Нужно проверить, равна ли на самом деле одна другой. Возможно, одна из них просто немного сдвинута.

# Пользователь вводит две строки. Напишите программу, которая определяет, можно ли получить первую строку из второй циклическим сдвигом.

# Опционально: если получить можно, то выведите значение этого сдвига.

# Пример 1:
# Первая строка: abcd
# Вторая строка: cdab
# Первая строка получается из второй со сдвигом 2.

# Пример 2:
# Первая строка: abcd
# Вторая строка: cdba
# Первую строку нельзя получить из второй с помощью циклического сдвига.

text =input('Первая строка: ')
text_2 =input('Вторая строка: ')
count = 0
if len(text) == len(text_2):
    for i in range(len(text_2)):
        count += 1
        text_2 = text_2[-1] + text_2[:-1]
        if text == text_2:
            print(f'Первая строка получается из второй со сдвигом {count}.')
            break
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

