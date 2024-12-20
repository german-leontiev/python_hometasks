# Задача 6. Сжатие
# Что нужно сделать
# С увеличением объёма данных возникла потребность в сжатии этих данных без потери важной информации. 
# Для этого было придумано кодирование, которое осуществляется следующим образом:

# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', 
# то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на экран. 
# Кодирование должно учитывать регистр символов.

# Пример:
# Введите строку: aaAAbbсaaaA

# Закодированная строка: a2A2b2с1a3A1

text = input('Введите строку: ')

encoded_text = ''
current_char = text[0]
count = 1

for i in range(1, len(text)):
    if text[i] == current_char:
        count += 1
    else:
        encoded_text += current_char + str(count)
        current_char = text[i]
        count = 1

encoded_text += current_char + str(count)

print('Закодированная строка:', encoded_text)
