# Задача 7. Двумерный список 
# Что нужно сделать
# Как мы говорили ранее, в программировании часто приходится писать код, исходя из результата, который требует заказчик. 
# В этот раз заказчику нужно получить такой двумерный список:

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Напишите программу, которая генерирует и выводит на экран такой список. Используйте только list comprehensions.


a =[[x + i for x in range(1,10,4)] for i in range(4)]
print(a)