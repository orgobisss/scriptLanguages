import math

# Запрос значений у пользователя
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

# Вычисление значения
z = math.log(x) + y**x + (5 * math.pi + 4.25 * x**2) / math.sqrt(abs(1 - 2 * y) + 5) - (y - a * b**2)**(1/3)

F = 2 * math.sqrt(abs(math.sin(2 * x) - math.cos(y)**2) / ((x**3 + y**3) * 0.25)) + math.exp(2 * x)

# Вывод результата
print(f"Результат вычисления 1 примера: {z}")

print(f"Результат вычисления 2 примера: {F}")
