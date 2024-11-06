import math

# Запрос значений у пользователя
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
d = float(input("Введите значение d: "))

# Вычисление значения
a = (math.sqrt(abs(0.25 - 2 * y**3)) + 4.25 * d**2) / ((y - x)**2 + 1) - math.exp(abs(4 * x - d)) * math.tan(2 * x)

u = 2**x + math.log(abs(math.atan(x) - math.sin(math.radians(58) * x))) + math.sqrt(x / (math.radians(58) * math.pi))

# Вывод результата
print(f"Результат вычисления 1 примера: {a}")

print(f"Результат вычисления 2 примера: {u}")