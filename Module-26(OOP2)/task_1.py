# Задача 1. Налоги
# Что нужно сделать
# Реализуйте иерархию классов, описывающих имущество налогоплательщиков. 
# Она должна состоять из базового класса Property и производных от него классов Apartment, Car и CountryHouse.

# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога, переопределённый в каждом из производных классов. 
# Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.

# Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.

# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества, 
# а затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).

class Property:

    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500


def main():
    print("Выберите тип имущества:")
    print("1. Квартира")
    print("2. Машина")
    print("3. Дача")
    
    choice = int(input("Введите номер: "))
    worth = float(input("Введите стоимость имущества: "))
    money = float(input("Введите количество ваших денег: "))

    if choice == 1:
        property_ = Apartment(worth)
    elif choice == 2:
        property_ = Car(worth)
    elif choice == 3:
        property_ = CountryHouse(worth)
    else:
        print("Недопустимый выбор")
        return
    
    tax = property_.calculate_tax()
    print(f"Налог на имущество: {tax}")
    if money < tax:
        print(f"Вам не хватает {tax - money} денег для оплаты налога")
    else:
        print("У вас достаточно денег для оплаты налога")

main()