import json
import os


# Функция для загрузки телефонного справочника из файла
def load_phonebook(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# Функция для сохранения телефонного справочника в файл
def save_phonebook(filename, phonebook):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, ensure_ascii=False, indent=4)


# Функция для добавления нового контакта
def add_contact(phonebook, name, phone_numbers):
    if name in phonebook:
        print(f"Контакт '{name}' уже существует. Добавляем номера к существующему контакту.")
        phonebook[name].extend(phone_numbers)
    else:
        phonebook[name] = phone_numbers
    print(f"Контакт '{name}' добавлен с номерами: {', '.join(phone_numbers)}")


# Функция для удаления контакта по имени
def delete_contact_by_name(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт '{name}' удален.")
    else:
        print(f"Контакт '{name}' не найден.")


# Функция для поиска контакта по номеру телефона
def search_contact_by_phone(phonebook, phone_number):
    for name, numbers in phonebook.items():
        if phone_number in numbers:
            return name, numbers
    return None


# Функция для удаления номера телефона из контактов
def delete_phone_number(phonebook, name, phone_number):
    if name in phonebook:
        if phone_number in phonebook[name]:
            phonebook[name].remove(phone_number)
            print(f"Номер '{phone_number}' удален из контакта '{name}'.")
            # Если больше нет номеров у контакта, можно удалить контакт
            if not phonebook[name]:
                del phonebook[name]
                print(f"Контакт '{name}' удален, так как у него больше нет номеров.")
        else:
            print(f"Номер '{phone_number}' не найден у контакта '{name}'.")
    else:
        print(f"Контакт '{name}' не найден.")


# Основной код
if __name__ == "__main__":
    filename = 'phonebook.json'

    # Загрузка телефонного справочника
    phonebook = load_phonebook(filename)

    # Примеры использования функций
    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Удалить контакт по имени")
        print("3. Поиск контакта по номеру телефона")
        print("4. Удалить номер телефона из контактов")
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            name = input("Введите имя контакта: ")
            phone_numbers = input("Введите номера телефонов через запятую: ").split(',')
            # Убираем лишние пробелы вокруг номеров
            phone_numbers = [number.strip() for number in phone_numbers]
            add_contact(phonebook, name, phone_numbers)
            save_phonebook(filename, phonebook)

        elif choice == '2':
            name = input("Введите имя контакта для удаления: ")
            delete_contact_by_name(phonebook, name)
            save_phonebook(filename, phonebook)

        elif choice == '3':
            phone_number = input("Введите номер телефона для поиска: ")
            result = search_contact_by_phone(phonebook, phone_number)
            if result:
                name, numbers = result
                print(f"Контакт найден: {name}, Номера: {', '.join(numbers)}")
            else:
                print("Контакт не найден.")

        elif choice == '4':
            name = input("Введите имя контакта: ")
            phone_number = input("Введите номер телефона для удаления: ")
            delete_phone_number(phonebook, name, phone_number)
            save_phonebook(filename, phonebook)

        elif choice == '5':
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")