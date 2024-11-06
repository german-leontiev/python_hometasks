print('Задача 3. Микроволновка')

choice =0
reverse_timer =int(input("Введите время приготовления: "))
for time in range(reverse_timer, 0, -1):
    print('Время приготовления: ', time)
    choice =int(input('Хотите забрать еду? (1 - да )(0 - нет)) '))
    if choice == 1:
        print('Ваша еда готова, можете забрать')
        print('на таймере осталось: ', time, 'секунд')
        break
    else:
        print('Ваша еда готова, осторожно горячo!')