# Задача 4. Компания
# Что нужно сделать
# Реализуйте иерархию классов, описывающих служащих в компании. 
# На самом верху иерархии — класс Person, который описывает человека именем, фамилией и возрастом. Все атрибуты этого класса являются приватными.

# Далее идёт класс Employee и производные от него классы Manager, Agent и Worker.

# Класс «Работник» должен иметь метод расчёта заработной платы, переопределённый в каждом из производных классов. 
# Заработная плата Manager постоянна и равна 13 000, заработная плата Agent определяется как оклад 5000 + 5% от объёма продаж, 
# который хранится в специальном поле класса Agent, а заработная плата Worker определяется как 100 * число отработанных часов, которое также хранится в отдельном поле.

# В основной программе создайте список из девяти объектов: первые три — Manager, следующие три — Agent и последние три — Worker. 
# Выведите на экран величину заработной платы всех девяти служащих.

from random import choice
from random import randint

class Person:

    def __init__(self, name, sur, age):
        self.__name = name
        self.__sur = sur
        self.__age = age

    def __str__(self):
        return f'Имя,Фамилия: {self.__name} {self.__sur} \tВозраст {self.__age}'

    def set_age(self, age):
        if age in range(10, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')

class Employee(Person):

    def __init__(self, name, sur, age):
        super().__init__(name, sur, age)

    def calc(self):
        pass

    def __str__(self):
        return super().__str__() + f'\nЗарплата {self.salary}'

class Manager(Employee):

    def __init__(self, name, sur, age):
        super().__init__(name, sur, age)
        self.salary = self.calc()

    def calc(self):
        return 13000

class Agent(Employee):
    def __init__(self, name, sur, age, sales):
        super().__init__(name, sur, age)
        self.sales = sales
        self.salary = self.calc()

    def calc(self):
        return 5000 + 0.05 * self.sales

class Worker(Employee):
    def __init__(self, name, sur, age, hours):
        super().__init__(name, sur, age)
        self.hours = hours
        self.salary = self.calc()

    def calc(self):
        return 100 * self.hours


names = ['Чертила', 'Влагоустойчивый', 'Хэр', 'Hometask', 'Windows']
surs = ['Мягкий', 'Терминал', 'Сбер-Спасибо', 'Кеш-бек', 'Анал']

def gen_pers():
    name = choice(names)
    sur = choice(surs)
    age = randint(18, 90)
    return name, sur, age

rabotnik = []
for i in range(3):
    name, sur, age = gen_pers()
    rabotnik.append('\nМэнеджер')
    rabotnik.append(Manager(name, sur, age))

for i in range(3):
    name, sur, age = gen_pers()
    rabotnik.append('\nАгент')
    rabotnik.append(Agent(name, sur, age,randint(1000, 10000)))

for i in range(3):
    name, sur, age = gen_pers()
    rabotnik.append('\nРаботник')
    rabotnik.append(Worker(name, sur, age, randint(10, 90)))

for i in rabotnik:
    print(i)