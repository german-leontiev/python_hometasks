# Задача 1. Ревью кода
# Ваня работает middle-разработчиком на Python в IT-компании. Один кандидат на junior-разработчика прислал ему код тестового задания. 
# Задание состояло в следующем: есть словарь из трёх студентов. Необходимо:

# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: 
# полный список интересов всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде эта функция вызывается, и значения присваиваются отдельным переменным, которые после выводятся на экран. 
# (Т.е. нужно распаковать все возвращаемые значения в отдельные переменные.)
# Ваня — очень придирчивый программист, и после просмотра кода он понял, что этого кандидата на работу не возьмёт, 
# даже несмотря на то, что он выдаёт верный результат. 
# Вот сам код кандидата:u

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt

# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])

# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)



student = []
for i_id,i_age in enumerate(students):
    print(f'id студента: {i_id + 1},возвраст: {students[i_age]['age']}')

def main(students):
    interes = []
    string = ''
    for i in students:
        interes += students[i]['interests']
        string += students[i]['surname']
    count = len(string)
    return count,interes

hobbi = main(students)[0]
surname_len = main(students)[1]
print(hobbi,surname_len)
