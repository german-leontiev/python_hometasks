# Задача 7. Продвинутая функция sum
# Что нужно сделать
# Как вы знаете, в Python есть полезная функция sum, которая умеет находить сумму элементов списков. 
# Но иногда базовых возможностей функций не хватает для работы и приходится их усовершенствовать.

# Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная функция sum. Она должна уметь:

# складывать числа из списка списков;
# складывать числа из набора параметров.
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

# Примеры вызовов функции:

# sum([[1, 2, [3]], [1], 3])

# Ответ в консоли: 10

# sum(1, 2, 3, 4, 5)

# Ответ в консоли: 15

def sum(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, list):  
            total_sum += sum(*arg) 
        elif isinstance(arg, (int, float)):  
            total_sum += arg 
    return total_sum



print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))