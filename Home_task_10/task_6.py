print('Задача 6. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant рублей,
# а расходы на проживание превышают стипендию и составляют expenses рублей в месяц.

# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Обратите внимание, что каждый месяц цены увеличиваются на 3% относительно прошлого месяца.

# Составьте программу расчёта суммы денег,
# которую необходимо получить у родителей один раз в начале обучения, чтобы можно было прожить учебный год (десять месяцев),
# используя только эти деньги и стипендию.

# Обратите внимание: во всех расчётах программы используются только целые числа, а дробные значения преобразуются в целые.

# Пример
# Введите ежемесячную стипендию: 10000
# Введите ежемесячные расходы: 12000
# 1-й месяц: траты 12000 рублей, не хватает 2000 рублей.
# 2-й месяц: траты 12360 рублей, не хватает 2360 рублей.
# 3-й месяц: траты 12730 рублей, не хватает 2730 рублей.
# 4-й месяц: траты 13111 рублей, не хватает 3111 рублей.
# 5-й месяц: траты 13504 рублей, не хватает 3504 рублей.
# 6-й месяц: траты 13909 рублей, не хватает 3909 рублей.
# 7-й месяц: траты 14326 рублей, не хватает 4326 рублей.
# 8-й месяц: траты 14755 рублей, не хватает 4755 рублей.
# 9-й месяц: траты 15197 рублей, не хватает 5197 рублей.
# 10-й месяц: траты 15652 рублей, не хватает 5652 рублей.
# Сумма денег, которую необходимо получить у родителей: 37544 рублей.

money = 0
educational_grant =int(input('Введите стипендию: '))
expenses =int(input('Введите расходы на проживание: '))
for month in range(1,10 +1):
    money += educational_grant
    money -= expenses
    print(month,'месяц траты', expenses, 'не хватает', -money)
    expenses += expenses //100 * 3
print('Нужно попросить у родителей ',-money ,'рублей')


