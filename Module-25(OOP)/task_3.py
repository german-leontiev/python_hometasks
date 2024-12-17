# Задача 3. Круг
# Что нужно сделать
# На координатной плоскости рисуются круги, у каждого круга следующие параметры: координаты X и Y центра круга и значение R ― радиус круга. 
# По умолчанию центр находится в (0, 0), а радиус равен 1.

# Реализуйте класс «Круг», который инициализируется по этим параметрам. Круг также может:
# Находить и возвращать свою площадь.
# Находить и возвращать свой периметр.
# Увеличиваться в K раз.
# Определять, пересекается ли он с другой окружностью.

class Circle:
    pi = 3.14159
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
 
    def get_area(self):
        return self.r * self.r * self.pi
 
    def get_perimeter(self):
        return 2 * self.r * self.pi
 
    def scale(self, k):
        self.r *= k
 
    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2

circle1 =Circle(1,1,15)
circle2 =Circle(2,2,16)

print("Площадь круга 1:", circle1.get_area())
print("Периметр круга 1:", circle1.get_perimeter())

circle1.scale(2)
print("Площадь круга 1 после масштабирования:", circle1.get_area())
print("Периметр круга 1 после масштабирования:", circle1.get_perimeter())

print("Пересекаются ли круги?", "Да" if circle1.is_intersect(circle2) else "Нет")