# Задача 1. Меню ресторана
# Что нужно сделать
# Один ресторан заказал вам написать приложение, которое по одному клику отображало бы пользователю доступное меню в удобном виде. 
# Для этого ресторан любезно предоставил свой сайт, откуда можно получить актуальную информацию о меню в виде идущих подряд названий.

# Напишите программу, которая выводит меню на экран. 
# На вход подаётся строка из названий блюд, разделённых символом «;», а на выходе эти названия перечисляются через запятую и пробел.

# Пример:
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов
# На данный момент в меню есть: утиное филе, фланк-стейк, банановый пирог, плов

menu =  'утиное филе','фланк-стейк','банановый пирог','плов'

print('Доступное меню:',';'.join(menu))
print(' На данный момент в меню есть:',', '.join(menu))

p ='acdc'
p = p[-1] + p[:-1]
print(p)