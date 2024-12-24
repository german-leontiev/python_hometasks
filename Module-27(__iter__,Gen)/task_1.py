# Задача 1. Квадраты чисел
# Что нужно сделать
# Пользователь вводит число N. 
# Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). 
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.

class Iter:
    """Итератор"""
    def __init__(self,num):
        self.__num = num
        self.__counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__counter < self.__num:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration
        

a = Iter(10)
print('Итератор: ')
for i in a:
    print(i, end =' ')



def Gen(num):
    """Генератор"""
    for i in range(1, num +1):
        yield i ** 2

print('\nГенератор: ')
for i in Gen(10):
    print(i, end= ' ')



value =(i ** 2 for i in range(1,11))
"""Выражение"""
print('\nВыражение: ')
for i in value:
    print(i, end= ' ')

