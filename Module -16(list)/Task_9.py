# Задача 9. Анализ слова 2
# Что нужно сделать
# Продолжите писать анализаторы для текста. 
# Теперь необходимо реализовать код, с помощью которого можно определять палиндромы — слова, которые одинаково читаются слева направо и справа налево.

# Напишите такую программу.

# Пример 1:

# Введите слово: мадам
# Слово является палиндромом

# Пример 2:

# Введите слово: abccba
# Слово является палиндромом

# Пример 3:

# Введите слово: abbd
# Слово не является палиндромом


word =input('Введите слово: ')
word = list(word)

count = 1

new_word = []

for i in range(len(word)):
    index = word[- count]
    count += 1
    new_word.append(index)

if new_word == word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

