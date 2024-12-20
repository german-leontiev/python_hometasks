# Задача 3. Функция
# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент (его можно вводить с клавиатуры). 
# Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно. 

# Если элемента нет вовсе — вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идёт до конца исходного.

cort =('zasd', 1, 2, 3, 4, 5, 'zxczxc', 1, 'fghfgh', 1, 2, 3, 4, 4, 'kto pisal zada4y?')

# print(cort)
element =  2


# def main(cort,element):
#     if element not in cort:
#         return ()
#     elif element in cort:
#         return cort[cort.index(element):cort.index(element,cort.index(element)+1)+1]
        
# print(main(cort,element))
               

element = 3   

def main(cort, element):
    new_cort = ()
    counter = 0

    for value in cort:
        if value is element:
            counter += 1 
        if counter == 1:
            new_cort += (value,)
        elif counter == 2:
            new_cort += (value,)
            return new_cort
    return new_cort

print(main(cort,element))