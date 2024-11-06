def safe_append(lst, item):
    if not isinstance(lst, list):
        return "Ошибка: Первый аргумент должен быть списком."

    lst.append(item)
    return lst

# Примеры использования
result1 = safe_append([1, 2, 3], 4)
print("Ваш список: ", result1)

result2 = safe_append("не список", 4)
print("Ваш список: ", result2)