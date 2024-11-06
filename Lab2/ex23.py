import math


def calculate_square_root(number):
    if number < 0:
        return "Ошибка: Невозможно вычислить квадратный корень отрицательного числа."


    return math.sqrt(number)

# Примеры использования
result = float(input("Введите число: "))
print(f"Корень: {calculate_square_root(result)}")