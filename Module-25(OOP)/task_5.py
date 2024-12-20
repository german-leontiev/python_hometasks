# Задача 5. Весёлая ферма —2
# Что нужно сделать
# Мы продолжаем писать игру «Весёлая ферма», и теперь необходимо её немного модернизировать. 
# Всё-таки кому-то нужно собирать урожай, и для этого нам понадобится садовник, у которого есть:

# Имя.
# Грядка с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
# И он может:

# Ухаживать за грядкой.
# Собирать с неё урожай (количество картошки ― пустой список).
# Модернизируйте программу, используя новый класс «Садовник». На всякий случай даём описание картошки и грядки.

# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и расти. 
# Всего у картошки может быть четыре стадии зрелости.

# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку, 
# а также предоставлять информацию о зрелости всей картошки на своей территории.

# Проверьте работу программы, создав грядку из пяти картошек и отдав эту грядку садовнику. 
# Пусть поухаживает за грядкой и соберёт урожай (может быть, даже и не один).
 

class Potato:
    states ={0:'Отсутсвует', 1: 'Росток',2: 'Зеленая',3: 'Зрелая'}


    def __init__(self,index):
        self.state = 0
        self.index = index

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.info()

    def info(self):
        print(f'Картошка {self.index} сейчас {self.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class Garden:

    def __init__(self,count):
        self.potatoes = [Potato(index) for index in range(1, count +1)]
    
    def grow_all(self):
        print('Картошка прорастает')
        for i in self.potatoes:
            i.grow()
    
    def are_all_ripe(self):
        if not all([i.is_ripe() for i in self.potatoes]):
            return False
        else:
            return True

class Man:

    def __init__(self,name,garden):
        self.name = name
        self.garden = garden
        self.man_pack = []
        
    def check(self):
        self.garden.grow_all()

    def action(self):
        if self.garden.are_all_ripe():
            print('Можно собирать')
            self.man_pack.append(len(self.garden.potatoes))
            self.garden = Garden(5)
        else:
            print('Еще рано')

    def loot(self):
        print(f'\nКолличество картошки: {sum(self.man_pack)}')
        
man = Man('sak',Garden(5))
for i in range(3):
    man.check()

man.action()
man.loot()