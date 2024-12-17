# Задача 2. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов). 
# Затем создайте список из десяти студентов 
# (данные о студентах можете придумать свои или запросить их у пользователя) и отсортируйте его по возрастанию среднего балла. 
# Выведите результат на экран.

import random




class Student:

    def __init__(self,name, num, balls=None):
        self.name = name
        self.num = num
        self.balls = balls if balls is not None else []

    def middleball(self):
        return sum(i for i in self.balls) / len(self.balls)

    def info(self):
        print(f'\nИмя: {self.name}\nГруппа: {self.num}\nБалл:{self.middleball()}')


st_list = []

st_list.append(['Сын Оргазма',1,[random.randint(1,5) for i in range(5)]])

st_list.append(['Мамут Рахал',2,[random.randint(1,5) for i in range(5)]])

st_list.append(['Человек Яйца',3,[random.randint(1,5) for i in range(5)]])

st_list.append(['Унтер Югент',4,[random.randint(1,5) for i in range(5)]])

st_list.append(['Героиновый Соперник',5,[random.randint(1,5) for i in range(5)]])

st_list.append(['Сырок Дружба',1,[random.randint(1,5) for i in range(5)]])

st_list.append(['Влага Сыровата',2,[random.randint(1,5) for i in range(5)]])

st_list.append(['Сижу Пержу',3,[random.randint(1,5) for i in range(5)]])

st_list.append(['Выйди Розбийник',4,[random.randint(1,5) for i in range(5)]])

st_list.append(['Запах Жопы',5,[random.randint(1,5) for i in range(5)]])


students = []
for i in range(len(st_list)):
    students.append(Student(st_list[i][0],st_list[i][1],st_list[i][2]))

sort_list = sorted(students, key=lambda x: x.middleball())

for i in sort_list:
    i.info()
