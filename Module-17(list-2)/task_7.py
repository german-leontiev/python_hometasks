# Задача 7. Ролики
# Что нужно сделать
# Частная контора даёт в прокат ролики разных размеров. Человек может надеть ролики только своего размера.

# Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей. 
# Реализуйте код, который определяет наибольшее число человек, которые могут одновременно взять ролики и пойти кататься.

# Пример:
# Кол-во коньков: 4
# Размер 1-й пары: 41
# Размер 2-й пары: 40
# Размер 3-й пары: 39
# Размер 4-й пары: 42

# Кол-во людей: 3
# Размер ноги 1-го человека: 42
# Размер ноги 2-го человека: 41
# Размер ноги 3-го человека: 42

# Наибольшее кол-во людей, которые могут взять ролики: 2

kon_list =[]
leg_list =[]
kon =int(input('Кол-во коньков: '))
for i in range(kon):
    kon_size =int(input(f'Размер {i +1} пары: '))
    kon_list.append(kon_size)

leg =int(input('Кол-во людей: '))
for i in range(leg):
    leg_size =int(input(f'Размер ноги {i +1} человека: '))
    leg_list.append(leg_size)

count = 0
for i in leg_list:
    for a in kon_list:
        if i == a:
            kon_list.remove(i)
            count += 1

print('Наибольшее кол-во людей, которые могут взять ролики: ', count)