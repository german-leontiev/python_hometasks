# Задача 2. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов). 
# Затем создайте список из десяти студентов 
# (данные о студентах можете придумать свои или запросить их у пользователя) и отсортируйте его по возрастанию среднего балла. 
# Выведите результат на экран.

import random

class Student:
    def __init__(self, name, num, balls=None):
        self.name = name
        self.num = num
        self.balls = balls if balls is not None else []

    def middleball(self):
        return sum(i for i in self.balls) / len(self.balls)

    def info(self):
        print(f'\nИмя: {self.name}\nГруппа: {self.num}\nБалл: {self.middleball()}')

students = [
    Student('Сын Оргазма', 1, [random.randint(1,5) for _ in range(5)]),
    Student('Мамут Рахал', 2, [random.randint(1,5) for _ in range(5)]),
    Student('Человек Яйца', 3, [random.randint(1,5) for _ in range(5)]),
    Student('Унтер Югент', 4, [random.randint(1,5) for _ in range(5)]),
    Student('Героиновый Соперник', 5, [random.randint(1,5) for _ in range(5)]),
    Student('Сырок Дружба', 1, [random.randint(1,5) for _ in range(5)]),
    Student('Влага Сыровата', 2, [random.randint(1,5) for _ in range(5)]),
    Student('Сижу Пержу', 3, [random.randint(1,5) for _ in range(5)]),
    Student('Выйди Розбийник', 4, [random.randint(1,5) for _ in range(5)]),
    Student('Запах Жопы', 5, [random.randint(1,5) for _ in range(5)])
]

sort_list = sorted(students, key=lambda x: x.middleball())

for student in sort_list:
    student.info()