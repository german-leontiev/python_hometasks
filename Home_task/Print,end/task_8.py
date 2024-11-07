print('Задача 8. Колонтитул')

text =input('Введите текст: ')
hz =int(input('введите общую длину колонтитула: '))
symbol =int(input('Введите желаемое количество восклицательных знаков: '))

hz1 = hz * '~'
symbol1 =symbol * '!'
print(hz1 + symbol1  + hz1)
print(hz * ' ' + text + hz * ' ')