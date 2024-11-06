def get_positive_integer():
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Ошибка: Число должно быть положительным.")
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное целое число.")

# Пример использования
print("Вы ввели положительное число: ", get_positive_integer())