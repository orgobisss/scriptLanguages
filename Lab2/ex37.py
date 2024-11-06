def get_valid_grade():
    while True:
        try:
            grade = int(input("Введите оценку от 1 до 5: "))

            if 1 <= grade <= 5:
                return grade
            else:
                raise ValueError("Оценка должна быть от 1 до 5.")

        except ValueError as e:
            if str(e) == "Оценка должна быть от 1 до 5.":
                print(f"Ошибка: {e} Попробуйте снова.")
            else:
                print("Ошибка: Введите целое число от 1 до 5. Попробуйте снова.")

        except Exception as e:
            print(f"Произошла неожиданная ошибка: {e}. Попробуйте снова.")


# Пример использования
user_grade = get_valid_grade()
print(f"Вы ввели оценку: {user_grade}")
