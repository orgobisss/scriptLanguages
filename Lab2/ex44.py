def sum_dict_values(data):
    if not isinstance(data, dict):
        return "Ошибка: Аргумент должен быть словарем."

    sum_dict = 0
    non_numeric = []

    for key, value in data.items():
        try:
            sum_dict += float(value)
        except (ValueError, TypeError):
            non_numeric.append(key)

    if non_numeric:
        return f"Сумма числовых значений: {sum_dict}."
    else:
        return f"Общая сумма: {sum_dict}"


# Примеры использования
result1 = sum_dict_values({'a': 1.6, 'b': 2.4, 'c': 3})
print("Пример 1: ", result1)

result2 = sum_dict_values({'a': 1, 'b': '2', 'c': 3, 'd': 'четыре'})
print("Пример 2: ", result2)

result3 = sum_dict_values([1, 2, 3])
print("Пример 3: ", result3)