# Задача 2. Самое длинное слово
# Что нужно сделать
# Пользователь вводит строку, содержащую пробелы. Найдите в ней самое длинное слово, выведите это слово и его длину. 
# Если таких слов несколько, выведите первое из них.

# Пример 1:
# Введите строку: я есть строка
# Самое длинное слово: строка
# Длина этого слова: 6

# Пример 2:
# Введите строку: а б
# Самое длинное слово: а
# Длина этого слова: 1

# Пример 3:
# Введите строку: б
# Самое длинное слово: б
# Длина этого слова: 1

text = input('Введите строки: ').split()
word = ''
for i in text:
    if len(word) < len(i):
        word = i

print('Самое длинное слово:', word)
print('Длина этого слова:', len(word))