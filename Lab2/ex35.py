def find_item_in_list(lst, item):
    try:
        if not isinstance(lst, list):
            raise TypeError("Первый аргумент должен быть списком")

        index = lst.index(item)
        return f"Элемент '{item}' найден в позиции {index}"
    except ValueError:
        return f"Элемент '{item}' не найден в списке"
    except TypeError as e:
        return f"Ошибка: {str(e)}"
    except Exception as e:
        return f"Произошла неожиданная ошибка: {str(e)}"


# Примеры использования
result1 = find_item_in_list([1, 2, 3, 4, 5], 3)
print("Пример 1: ", result1)

result2 = find_item_in_list([1, 2, 3, 4, 5], 6)
print("Пример 2: ", result2)

result3 = find_item_in_list("не список", 3)
print("Пример 3: ", result3)
