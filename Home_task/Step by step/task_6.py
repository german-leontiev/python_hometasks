print('Задача 6. Стипендия')

money = 0
educational_grant =int(input('Введите стипендию: '))
expenses =int(input('Введите расходы на проживание: '))
for month in range(1,10 +1):
    money += educational_grant
    money -= expenses
    print(month,'месяц траты', expenses, 'не хватает', -money)
    expenses += expenses //100 * 3
print('Нужно попросить у родителей ',-money ,'рублей')


