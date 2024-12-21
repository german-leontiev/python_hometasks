# Задача 2. Карма
# Что нужно сделать
# Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.

# Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:

# KillError;
# DrunkError;
# CarCrashError;
# GluttonyError;
# DepressionError.
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы до уровня константы. 
# Исключения обработайте и запишите в отдельный лог karma.log.

from random import choice
from random import randint

class KillError(Exception):
    """Опа, кого-то хлопнули"""
    pass

class DrunkError(Exception):
    """Опять нажрался"""
    pass

class CarCrashError(Exception):
    """ДТП, фура убила"""
    pass

class GluttonyError(Exception):
    """Объился окорочкив, а пахнэ як..."""
    pass

class DepressionError(Exception):
    """GG, тима даунов, 1 vs 9"""
    pass


class Monk:

    err = [KillError,DrunkError,CarCrashError,GluttonyError,DepressionError]

    def __init__(self,name,ascendancy = 0):
        self.name = name
        self.ascendancy = ascendancy
        
    def get_ascendancy(self):
        return self.ascendancy
    
    def increase_ascendancy(self, boost):
        self.ascendancy += boost
    



def one_day(count, monk):
    ne_povezlo = randint(1, 10)
    error = choice(Monk.err)
    if ne_povezlo == 1:
        with open('karma.log', 'a') as karma:
            karma.write(f'День: {count}    Что случилось - {error.__doc__}\n')
        raise error(f'На {count} день монах {monk.name} столкнулся с проблемой: {error.__doc__}')
    else:
        monk.increase_ascendancy(randint(1, 7))
        return True


monk = Monk('Зелемхан Пулеметчик')
count = 0
while monk.get_ascendancy() < 500:
    count += 1
    try:
        one_day(count, monk)
    except Exception as e:
        print(e)
    if monk.get_ascendancy() >= 500:
        print('Вы стали богом, но...')
        with open('karma.log', 'r') as karma:
            for i in karma:
                print(i)
        break

""""Чистка .txt"""
def clear_log(filename):
    with open(filename, 'w') as file:
        file.write('')
#clear_log('karma.log')