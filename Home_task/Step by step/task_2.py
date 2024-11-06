print('Задача 2. Долги')

money =0
idiot =int(input('Введите количество должников: '))
for idiot_number in range(0, idiot, 5):
    print('Должник с номером ', idiot_number,)
    money += int(input('Сколько должны? '))
print('Общая сумма долга: ',money)