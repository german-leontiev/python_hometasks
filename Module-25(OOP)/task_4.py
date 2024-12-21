# Задача 4. Отцы, матери и дети
# Что нужно сделать
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:

# Имя.
# Возраст.
# Список детей.
# И он может:

# Сообщить информацию о себе.
# Успокоить ребёнка.
# Покормить ребёнка.
# У ребёнка есть:

# Имя.
# Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# Состояние спокойствия.
# Состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё интереснее.

from random import choice


class Parent:
    
    def __init__(self,name,age,kid_lst= None):
        self.name = name
        self.age = age
        self.kid_lst = kid_lst if kid_lst is not None else []

    def info(self):
        print(f'\n{self.name} {self.age}')
        if self.kid_lst:
            print('Дети:')
            for i in self.kid_lst:
                print(f'{i.name} {i.age}: {i.sueta} и {i.eda}')

    def tishe(self):
        for i in self.kid_lst:
            if i.sueta == 'Баляя суету навести охото':
                print(f'\n{i.name} говорит: Баляя суету навести охото \n{self.name} угомонил пиздюка {i.name} ')
                i.sueta = 'Спокоен'

    def eat(self):
        for i in self.kid_lst:
            if i.eda == 'Голоден':
                print(f'\n{i.name} хочет "Вкусно и Точка"\n{self.name} покормил пиздюка {i.name}')
                i.eda = 'Сыт'

    def addkid(self,kid):
        if self.age - kid.age > 16: 
            self.kid_lst.append(kid) 
            print(f'{kid.name} Welkome to the club buddy.') 
        else: 
            print(f'{kid.name} слишком стар.') 

class Kid:
    eda = ['Голоден','Сыт']
    sueta = ['Баляя суету навести охото','Спокоен']

    def __init__(self,name,age,):
        self.name = name
        self.age = age
        self.eda = choice(Kid.eda)
        self.sueta = choice(Kid.sueta)



parent = Parent('Наруто',50)

kid = Kid('Мегатрон',10)
kid_2 = Kid('Сунь Цзи',15)
kid_3 = Kid('Хлеб про который я забыл',200)

parent.addkid(kid)
parent.addkid(kid_2)
parent.addkid(kid_3)
        
parent.eat()
parent.tishe()
parent.info()
        