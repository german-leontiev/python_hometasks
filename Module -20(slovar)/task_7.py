# Задача 7. Пицца
# В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, что и сколько заказывал у них в определённый период. 
# Вам нужно структурировать эту информацию, а также понять, сколько всего пицц купил каждый заказчик.

# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида «Покупатель — название пиццы — количество заказанных пицц». 
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту. Учитывайте, что один человек может заказать одно и то же несколько раз.

# Пример:

# Введите кол-во заказов: 6

# 1 заказ: Иванов Пепперони 1

# 2 заказ: Петров Де-Люкс 2

# 3 заказ: Иванов Мясная 3

# 4 заказ: Иванов Мексиканская 2

# 5 заказ: Иванов Пепперони 2

# 6 заказ: Петров Интересная 5



# Иванов: 

#     Мексиканская: 2

#     Мясная: 3

#     Пепперони: 3

# Петров:

#     Де-Люкс: 2

#     Интересная: 5


pizza ={}
count =int(input('Введите кол-во заказов: '))


for i in range(count):
    pers =input(f'{i +1} заказ: ').split()
    if pers[0] not in pizza:
        pizza[pers[0]] = dict({pers[1]:int(pers[2])}) 
    elif pers[1] in pizza[pers[0]]:
        pizza[pers[0]][pers[1]] += int(pers[2])
    else:
        pizza[pers[0]][pers[1]] = int(pers[2])


for i in sorted(pizza.keys()):
    print(i)
    for _ in sorted(pizza[i].keys()):
        print('   ',_, ':', pizza[i][_] )