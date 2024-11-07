print('Задача 9. Коровы')

milk_rate = 0
milk = 0
spawn =input('Введите 10 символов,где a — свободное стойло, b — занятое.: ')
for cow in spawn:
    milk_rate += 2
    if cow == 'a':
        milk += milk_rate
print('Кол-во молока за день :',  milk)