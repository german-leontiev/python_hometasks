print('Задача 8. Кинотеатр')
boys =int(input('Введите количество мальчиков: '))
girls =int(input('Введите количество девочек: '))
text = ""
if (boys > girls *2) or (girls > boys *2):
    print('Нет решения')