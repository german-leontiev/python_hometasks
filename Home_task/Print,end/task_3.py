print('Задача 3. Кривой мессенджер')

star =0
text =input('Введите текст: ')
for symbol in (text):
    if symbol != '*':
        star += 1
    else:
        print('Символ * стоит на позиции ', star +1)

