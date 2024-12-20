# Задача 6. Магия
# Что нужно сделать
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. 
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

# Вот таблица преобразований:

# «Вода» + «Воздух» = «Шторм»
# «Вода» + «Огонь» = «Пар»
# «Вода» + «Земля» = «Грязь»
# «Воздух» + «Огонь» = «Молния»
# «Воздух» + «Земля» = «Пыль»
# «Огонь» + «Земля» = «Лава»
# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс. 
# Если результат не определён, то возвращается None.

# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:

# class Example_1:
#     def __add__(self, other):
#         return Example_2()

# class Example_2:
#     answer = 'сложили два класса и вывели'

# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)

# Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.


class Storm:
    spell = 'Шторм'

class Steam:
    spell = 'Пар'

class Mud:
    spell = 'Грязюка'

class Lightning:
    spell = 'Ззап'

class Dust:
    spell = 'Пыль'

class Lava:
    spell = 'Лава'

class Gaming_chair:
    spell = 'Игровое кресло'

class Water:
    elem = 'Вода'

    def __add__(self,other):
        if other.elem == 'Воздух':
            return Storm()
        elif other.elem == 'Огонь':
            return Steam()
        elif other.elem == 'Земля':
            return Mud()
        else:
            return None
        
class Air:
    elem = 'Воздух'

    def __add__(self,other):
        if other.elem == 'Огонь':
            return Lightning()
        elif other.elem == 'Земля':
            return Dust()
        elif other.elem == 'Вода':
            return Storm()
        else:
            return None
            
class Fire:
    elem = 'Огонь'

    def __add__(self,other):
        if other.elem == 'Вода':
            return Steam()
        elif other.elem == 'Воздух':
            return Lightning()
        elif other.elem == 'Земля':
            return Lava()
        else:
            return None
        
class Earth:
    elem = 'Земля'

    def __add__(self,other):
        if other.elem == 'Вода':
            return Mud()
        elif other.elem == 'Воздух':
            return Dust()
        elif other.elem == 'Огонь':
            return Lava()
        
class Chair:
    elem = 'Стул'

    def __add__(self,other):
        if other.elem == 'Бутылка':
            return Gaming_chair
        elif other.elem == 'Огонь':
            return 'Дрова'
        else:
            return None
        
class Bottle:
    elem = 'Бутылка'

    def __add__(self,other):
        if other.elem == 'Стул':
            return Gaming_chair
        else:
            return None
        
a = Chair() + Bottle()
print(a.spell)

# Вода, Земля, Огонь, Воздух. Когда-то давно, четыре народа жили в мире. 
# Но вскоре народ огня развязал войну. Только Аватар – властелин всех четырёх стихий, мог остановить захватчиков. 
# Но когда мир нуждался в нём больше всего – он исчез.

