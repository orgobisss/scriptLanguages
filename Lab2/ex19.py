import os

def file_info(filename):
    try:
        # Проверка, существует ли файл
        if not os.path.exists(filename):
            return f"Ошибка: файл '{filename}' не существует."

        # Проверка, является ли это файлом
        if not os.path.isfile(filename):
            return f"Ошибка: '{filename}' не является файлом."

        # Получение информации о файле
        file_name = os.path.basename(filename)
        file_size = os.path.getsize(filename)

        return {
            "Имя файла": file_name,
            "Размер файла (в байтах)": file_size,
        }

    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


# Примеры использования
info1 = file_info("example.txt")
print(info1)

info2 = file_info("not_example.txt")
print(info2)