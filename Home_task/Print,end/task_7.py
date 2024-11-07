print('Задача 7. Великий и могучий')



symbol_count = 0
count = 0
text =input('Введите текст: ')
for symbol in text:
    count +=1
    if symbol == ' ':
        symbol_count = count
        count = 0
    elif count > count:
        break
print('Самое длинное слово, букв ', symbol_count)



