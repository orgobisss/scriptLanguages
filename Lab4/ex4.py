import math

# Базовый класс Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        # Вычисляет расстояние от точки до начала координат (0, 0)
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def getPoint(self):
        # Возвращает координаты точки в виде списка [x, y]
        return [self.x, self.y]

# Подкласс PointColor, наследующий Point
class PointColor(Point):
    def __init__(self, x, y, color):
        # Вызов конструктора базового класса
        super().__init__(x, y)
        self.color = color

    def getColor(self):
        # Возвращает цвет точки
        return self.color

# Примеры использования
point = Point(3, 4)
print("Координаты точки:", point.getPoint())  # Вывод: [3, 4]
print("Расстояние до начала координат:", point.distance_to_origin())  # Вывод: 5.0

colored_point = PointColor(5, 12, "red")
print("\nКоординаты цветной точки:", colored_point.getPoint())  # Вывод: [5, 12]
print("Цвет точки:", colored_point.getColor())  # Вывод: red
print("Расстояние до начала координат:", colored_point.distance_to_origin())  # Вывод: 13.0
