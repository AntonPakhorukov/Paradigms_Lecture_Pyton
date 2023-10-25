import math
class Rectangle:
    # Создаем метод __init__ который принимает self в качестве 
    # первого объекта и все что мы захотим в качестве остальных.
    def __init__(self, width, length): 
        # Далее мы хотим,чтобы эти длина и ширина стали атрибутами класса.   
        # обращение к классу изнутри (то есть “к самому себе”) 
        # реализуется через ключевое слово self.
        self.width = width
        self.length = length
    def calc_area(self):
        self.area = self.width * self.length
        return self.area
    def calc_perimetr(self):
        self.perimetr = 2 * (self.width + self.length)
        return self.perimetr
    def calc_diag_len(self):
        self.diag = (self.width ** 2 + self.length ** 2) ** 0.5
        return round(self.diag, 2)
    def calc_diag_angles(self):
        """
        вычисляет и возвращает два угла между диагоналями в градусах
        """
        # осуществляется проверка на наличия у данного объекта атрибута diag
        # встроенный метод hasattr принимает объект и имя атрибута
        # и возвращает True, если переданный атрибут существует в 
        # данномо бъекте
        if not hasattr(self, 'diag'):
            self.calc_diag_len()
        cos_diag_length = self.length / self.diag
        angle_diag_length = math.acos(cos_diag_length)
        angle_diag_length = math.degrees(angle_diag_length)
        first_angle = 180 - (2 * angle_diag_length)
        second_angle = (360 - 2 * first_angle) / 2
        assert (second_angle * 2 + first_angle * 2) == 360
        return round(first_angle, 2), round(second_angle, 2)
    
    # Переопределение встроенных операторов в пайтоне
    def __add__(self, other):
        return self.area + other.area
    
    def __eq__(self, other):
        return self.area == other.area
        
# Создаем прямоугольник
rect = Rectangle(4, 5)
# Распечатываем прямоугольник
print(rect.width, rect.length)
print(rect.calc_area())
print(rect.calc_perimetr())
print(rect.calc_diag_len())

print(f"Area: {rect.calc_area()}")
print(f"Perimetr: {rect.calc_perimetr()}")
print(f"Diagonal Length: {rect.calc_diag_len()}")
print(f"Angles diagonal: {rect.calc_diag_angles()}")
rect2 = Rectangle(5, 10)
rect2.calc_area()
# без переопределения __add__ пайтон не поймет, 
# как суммировать прямоугольники
print(rect.__add__(rect2)) 
print(rect + rect2) 
print(rect == rect2) # false
   