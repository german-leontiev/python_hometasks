print('Задача 1. Конвертация')

# При покупках за рубежом
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например, если оплачивать отечественной картой товар в евро,
# то сначала эта сумма конвертируется в доллары, а потом — в рубли.

# Напишите программу,
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.

# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рубля.

# Пример
# Стоимость покупки в евро: 25
# Стоимость в рублях: 1902.1875

eur =float(input('\nВведите стоимость покупки в евро: '))
print('Стоимость в рублях:', eur * 1.25 * 60.87)