# Задача 3. Свой словарь
# Что нужно сделать
# В силу обстоятельств Васе постоянно приходится работать со словарями и их данными. 
# В том числе и с методом get, который по умолчанию возвращает None, если такого ключа в словаре нет. 
# Однако Васю это не устраивает: для нормальной работы ему нужно возвращать число 0.

# Реализуйте класс MyDict, который будет вести себя точно так же, как и обычный словарь, 
# за исключением того, что метод get по умолчанию будет возвращать не None, а число 0.

class MyDict(dict):  

    def get(self, key):   
        return dict.get(self,key) or 0
    
d = MyDict({'a':1,'s':2,'d':3})
print(d.get('a'),d.get('d'))