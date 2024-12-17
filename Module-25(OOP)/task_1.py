# Задача 1. Драка
# Что нужно сделать
# Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:

# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. 
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. 
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. 
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

# Реализуйте такую программу.

import random


class Warrior:

    def __init__(self,name,hp = 100):
        self.name = name
        self.hp = hp

    def damage(self):
        self.hp -= 20
        print(f'{self.name} получил тычку. HP = {self.hp}')
        
    
warrior_1 = Warrior('KFC boec')
warrior_2 = Warrior('UFC boec')

while True:
    attack = random.randint(1,2)
    if attack == 1:
        print(f'\n{warrior_1.name} атакует')
        warrior_2.damage()
    elif attack == 2:
        print(f'\n{warrior_2.name} атакует')
        warrior_1.damage()
    if warrior_1.hp == 0:
        print(f'\n{warrior_2.name} победил!')
        break
    elif warrior_2.hp == 0:
        print(f'\n{warrior_1.name} победил!')
        break