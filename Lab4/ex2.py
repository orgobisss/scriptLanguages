class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def can_form_triangle(self):
        # Проверка условия существования треугольника
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def perimeter(self):
        if self.can_form_triangle():
            return self.a + self.b + self.c
        else:
            return None

    def show_triangle_info(self):
        if self.can_form_triangle():
            print("Можно построить треугольник!")
            print(f"Периметр треугольника равен = {self.perimeter()}\n")
        else:
            print("Треугольник не сделать из этого.\n")

# Класс EquilateralTriangle, наследующий Triangle
class EquilateralTriangle(Triangle):
    def __init__(self, side_length):
        # Использование конструктора базового класса
        super().__init__(side_length, side_length, side_length)

    def show_triangle_info(self):
        if self.can_form_triangle():
            print("Это равносторонний треугольник!")
            print(f"Периметр треугольника равен = {self.perimeter()}\n")
        else:
            print("Треугольник не сделать из этого.\n")

# Примеры использования
# Обычный треугольник
triangle = Triangle(3, 4, 5)
triangle.show_triangle_info()

# Равносторонний треугольник
equilateral_triangle = EquilateralTriangle(5)
equilateral_triangle.show_triangle_info()

# Треугольник с невозможными сторонами
invalid_triangle = Triangle(1, 2, 3)
invalid_triangle.show_triangle_info()