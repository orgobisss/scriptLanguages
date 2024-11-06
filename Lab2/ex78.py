import os

# Определяем путь к файлу для хранения списка книг
BOOKS_FILE = 'books.txt'


# Функция для загрузки списка книг из файла
def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []

    books = []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                # Каждая строка книги в формате: Название | Автор | Год
                title, author, year = line.strip().split(', ')
                books.append({
                    "title": title,
                    "author": author,
                    "year": int(year)
                })
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return books


# Функция для сохранения списка книг в файл
def save_books(books):
    try:
        with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
            for book in books:
                file.write(f"{book['title']}, {book['author']}, {book['year']}\n")
    except Exception as e:
        print(f"Ошибка при сохранении данных в файл: {e}")


# Функция для добавления книги
def add_book(title, author, year):
    try:
        age = int(year)  # Проверяем, что возраст — это число
    except ValueError:
        print("Ошибка: введите верно год.")
        return

    books = load_books()
    books.append({
        "title": title,
        "author": author,
        "year": year
    })
    save_books(books)
    print(f"Книга '{title}' добавлена.")


# Функция для удаления книги по названию
def remove_book(title):
    books = load_books()
    filtered_books = [book for book in books if book['title'].lower() != title.lower()]

    if len(books) == len(filtered_books):
        print(f"Книга '{title}' не найдена.")
    else:
        save_books(filtered_books)
        print(f"Книга '{title}' удалена.")


# Функция для поиска книги по названию
def find_book(title):
    books = load_books()
    found_books = [book for book in books if title.lower() in book['title'].lower()]

    if found_books:
        for book in found_books:
            print(f"Название: {book['title']}, Автор: {book['author']}, Год выпуска: {book['year']}")
    else:
        print(f"Книга '{title}' не найдена.")


# Функция для вывода всех книг
def list_books():
    books = load_books()
    if not books:
        print("Список книг пуст.")
    else:
        print("\nСписок книг:")
        for book in books:
            print(f"Название: {book['title']}, Автор: {book['author']}, Год выпуска: {book['year']}")


# Основное меню программы
def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год выпуска: ")
            add_book(title, author, year)
        elif choice == '2':
            title = input("Введите название книги, которую хотите удалить: ")
            remove_book(title)
        elif choice == '3':
            title = input("Введите название книги для поиска: ")
            find_book(title)
        elif choice == '4':
            list_books()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


# Запуск программы
menu()