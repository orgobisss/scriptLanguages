# Запрос значений у пользователя
input_a = float(input("Введите значение a: "))
input_b = float(input("Введите значение b: "))

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."

# Примеры использования
print(f"Результат деления: {divide(input_a, input_b)}")