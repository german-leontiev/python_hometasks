# Задача 7. Совместное проживание
# Что нужно сделать
# Чтобы понять, стоит ли ему жить с кем-то или всё же лучше остаться в гордом одиночестве, Артём решил провести довольно необычное исследование. 
# Для этого он реализовал модель человека и модель дома.

# Человек может:

# Есть (+ сытость, − еда).
# Работать (− сытость, + деньги).
# Играть (− сытость).
# Ходить в магазин за едой (+ еда, − деньги).
# У человека есть имя, степень сытости (изначально 50) и дом.

# В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами (изначально 0 денег).

# Если сытость человека становится меньше нуля, то человек умирает.

# Логика действий человека определяется следующим образом:

# Генерируется число кубика от 1 до 6.
# Если сытость < 20, то поесть.
# Иначе, если еды в доме < 10, то сходить в магазин.
# Иначе, если денег в доме < 50, то работать.
# Иначе, если кубик равен 1, то работать.
# Иначе, если кубик равен 2, то поесть.
# Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.

# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.



from random import randint, choice
 
class House:
        food = 50
        money = 0
 
 
class Person:
    
    def __init__(self, name):
        self.name = name
        self.satiety = 50
 
    def eat(self): 
        self.satiety += 1
        House.food -= 1
        return f'ест, сытость: {self.satiety} еда: {House.food}'
 
    def work(self): 
        self.satiety -= 1
        House.money += 1
        return f'работает, сытость: {self.satiety} деньги: {House.money}'
 
    def play(self): 
        self.satiety -= 1
        return f'играет в доту, сытость {self.satiety}'
        
    def repast(self): 
        House.food += 1
        House.money -= 1
        return f'идет в магазин, еда: {House.food} деньги: {House.money}'
 
person_1 = Person('Артём')
person_2 = Person('Адольф')
 
def play(person):
        number_cubes = randint(1,6)
        if person.satiety < 0:
                print(f'К сожалению, {person.name} помер с голоду ')
                return 1
        if person.satiety < 20 and House.food >= 10:
                text = person.eat()
        elif House.food < 10:
                text = person.repast()
        elif House.money < 50:
                text = person.work()
        elif number_cubes == 1:
                text = person.work()
        elif number_cubes == 2:
                text = person.eat()
        else:
                text = person.play()
        print(person.name, text)
        return 0
 
 
for i in range(365):
    if play(person_1) or play(person_2):
            print('GG')
if i == 364:    
        print('выжили')