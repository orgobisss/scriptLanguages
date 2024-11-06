class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getXY(self):
        # Возвращает координаты в виде списка
        return [self.x, self.y]

    def __add__(self, other):
        # Перегрузка оператора сложения
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def show(self):
        # Выводит координаты точки
        print(f"Координаты точки: ({self.x}, {self.y})")

# Примеры использования
point1 = Point(2, 3)
point2 = Point(4, 5)

# Сложение точек
result_point = point1 + point2

# Вывод результата
point1.show()  # Вывод: Координаты точки: (2, 3)
point2.show()  # Вывод: Координаты точки: (4, 5)
result_point.show()  # Вывод: Координаты точки: (6, 8)

# Получение координат в виде списка
print(point1.getXY())  # Вывод: [2, 3]
print(point2.getXY())  # Вывод: [4, 5]
print(result_point.getXY())  # Вывод: [6, 8]
