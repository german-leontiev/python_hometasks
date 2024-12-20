# Задача 2. Универсальная программа 2
# Спустя некоторое время заказчик попросил нас немного изменить скрипт для своей криптографии: теперь индексы элементов должны быть простыми числами.

# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря), у которых индекс — это простое число. 
# Для проверки на простое число напишите отдельную функцию is_prime.

# Дополнительно: сделайте так, чтобы основная функция состояла только из оператора return и при этом также возвращала список.

def is_prime(number):

    if number < 2:
        return False

    for div in range(number - 1, 1, -1):
        if number % div == 0:
            return False
    return True
        

def main(iter_obj):
    return  [v for i, v in enumerate(iter_obj) if is_prime(i)]




