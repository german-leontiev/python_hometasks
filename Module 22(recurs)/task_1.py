# Задача 1. Challenge — 2
# Что нужно сделать
# Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой задачу, но не сильно связанную с математикой, 
# а именно: написать функцию, которая выводит все числа от 1 до num без использования циклов. Помогите другу реализовать такую функцию.

# Пример работы программы

# Введите num: 10

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

def main(num):
    if num < 1:
        return
    main(num -1)
    print(num)

    
a =int(input('Введите num: '))
main(a)