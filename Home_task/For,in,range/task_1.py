print('Задача 1.  Космический корабль')

# На космическом корабле каждый пассажир получает уникальный номер для идентификации.
# Эти номера всегда были положительными числами. Однако во время полёта произошёл сбой системы, и некоторые номера стали отрицательными.
# Для следующего этапа путешествия капитан должен отобрать только тех пассажиров, кто имеет положительные и чётные номера.

# Напишите программу, которая при вводе десяти чисел определяет,
# сколько из них являются одновременно чётными и положительными.

# Пример
# Введите номер человека: 2
# Введите номер человека: 3
# …
# …
# …
# Количество корректных номеров (чётных и положительных): 8
positive = 0
for man in range(10):
    man =int(input('Введите номер человека: '))
    if man % 2 == 0 and man > 0:
        positive += 1
print('Количество корректных номеров (чётных и положительных): ', positive)