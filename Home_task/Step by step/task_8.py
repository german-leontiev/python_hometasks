print('Задача 8. Кинотеатр')
# Что нужно сделать
# X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд места в одном ряду. Напишите программу, которая
# выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым мальчиком сидела хотя бы одна девочка, а рядом с каждой
# девочкой — хотя бы один мальчик.
# На вход подаются два числа: количество мальчиков X и количество девочек Y. В ответе выведите какую-нибудь строку, в которой
# будет ровно X символов B, обозначающих мальчиков, и Y символов G, обозначающих девочек, удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно. Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку «Нет решения».
# Пример 1
# Введите количество мальчиков: 5
# Введите количество девочек: 5
# Ответ: BGBGBGBGBG
boys =int(input('Введите количество мальчиков: '))
girls =int(input('Введите количество девочек: '))
text = ""
if (boys > girls *2) or (girls > boys *2):
    print('Нет решения')