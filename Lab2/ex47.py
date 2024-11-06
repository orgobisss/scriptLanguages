class InvalidDataError(Exception):
    pass


def validate_data(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Входные данные должны быть словарем")

        required_keys = ['name', 'age', 'email']
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует обязательное поле: {key}")

        # Проверка возраста
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise InvalidDataError("Возраст должен быть целым положительным числом")

        # Проверка email
        if not isinstance(data['email'], str) or '@' not in data['email']:
            raise InvalidDataError("Некорректный формат email")

        print("Данные в словаре:", data)
    except (InvalidDataError, TypeError, KeyError) as e:
        print(f"Ошибка: {e}.")


# Примеры использования
valid_data1 = {'name': 'Анна', 'age': 30, 'email': 'example@gmail.com'}
validate_data(valid_data1)


# Примеры использования
valid_data2 = {'name': 'Илья', 'age': -5, 'email': 'example@yandex.com'}
validate_data(valid_data2)


not_a_dict2 = [1, 2, 3]
validate_data(not_a_dict2)


missing_key = {'name': 'Петр', 'age': 25}
validate_data(missing_key)