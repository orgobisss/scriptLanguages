import os

# Определяем путь к файлу для хранения данных студентов
STUDENTS_FILE = 'students.txt'


# Функция для загрузки данных студентов из файла
def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []

    students = []
    try:
        with open(STUDENTS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                # Каждая строка студента в формате: Имя | Возраст | Группа
                name, age, group = line.strip().split(', ')
                students.append({
                    "name": name,
                    "age": int(age),
                    "group": group
                })
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return students


# Функция для сохранения данных студентов в файл
def save_students(students):
    try:
        with open(STUDENTS_FILE, 'w', encoding='utf-8') as file:
            for student in students:
                file.write(f"{student['name']}, {student['age']}, {student['group']}\n")
    except Exception as e:
        print(f"Ошибка при сохранении данных в файл: {e}")


# Функция для добавления нового студента
def add_student(name, age, group):
    try:
        age = int(age)  # Проверяем, что возраст — это число
    except ValueError:
        print("Ошибка: введите верно возраст.")
        return

    students = load_students()
    students.append({
        "name": name,
        "age": age,
        "group": group
    })
    save_students(students)
    print(f"Студент {name} добавлен.")


# Функция для редактирования информации о студенте
def edit_student(name):
    students = load_students()
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Текущая информация: Имя: {student['name']}, Возраст: {student['age']}, Группа: {student['group']}")
            new_name = input("Введите новое имя (Enter для пропуска): ")
            new_age = input("Введите новый возраст (Enter для пропуска): ")
            new_group = input("Введите новую группу (Enter для пропуска): ")

            if new_name:
                student['name'] = new_name
            if new_age:
                try:
                    student['age'] = int(new_age)  # Проверяем, что возраст — это число
                except ValueError:
                    print("Ошибка: возраст должен быть числом.")
                    return
            if new_group:
                student['group'] = new_group

            save_students(students)
            print(f"Информация о студенте {name} обновлена.")
            return

    print(f"Студент с именем {name} не найден.")


# Функция для вывода всех студентов
def list_students():
    students = load_students()
    if not students:
        print("Список студентов пуст.")
    else:
        print("\nСписок студентов:")
        for student in students:
            print(f"Имя: {student['name']}, Возраст: {student['age']}, Группа: {student['group']}")


# Основное меню программы
def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Редактировать информацию о студенте")
        print("3. Показать список студентов")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя студента: ")
            age = input("Введите возраст студента: ")
            group = input("Введите группу студента: ")
            add_student(name, age, group)
        elif choice == '2':
            name = input("Введите имя студента для редактирования: ")
            edit_student(name)
        elif choice == '3':
            list_students()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


# Запуск программы
menu()
