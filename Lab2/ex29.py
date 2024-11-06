def write_list_to_file(filename, lst):
    try:
        if not isinstance(lst, list):
            raise TypeError("Второй аргумент должен быть списком")

        with open(filename, 'w') as file:
            for item in lst:
                file.write(str(item) + '\n')
        return f"Список успешно записан в файл {filename}"
    except IOError as e:
        return f"Ошибка при записи в файл: {str(e)}"
    except TypeError as e:
        return f"Ошибка: {str(e)}"
    except Exception as e:
        return f"Произошла неожиданная ошибка: {str(e)}"


# Примеры использования
result1 = write_list_to_file("file.txt", [1, 2, 3, 4, 5])
print("Пример 1: ", result1)

result2 = write_list_to_file("file.txt", "не список")
print("Пример 2: ", result2)

result3 = write_list_to_file("/lab/python/file.txt", [1, 2, 3, 4, 5])
print("Пример 3: ", result3)