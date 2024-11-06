# Функция для записи названий фильмов в файл
def write_movies_to_file(filename, movies):
    with open(filename, 'w') as file:
        for i in range(0, len(movies), 3):  # Проходим по списку с шагом 3
            line = movies[i:i + 3]  # Берем подсписок из трех элементов
            file.write(' | '.join(line) + '\n')  # Записываем их в файл, разделяя символом ' | '


# Функция для чтения содержимого файла и вывода на экран
def read_and_print_file(filename):
    with open(filename, 'r') as file:
        movie = file.read()
        print(movie)


# Укажите имя файла
filename = 'movies.txt'

# Список названий фильмов
movies = [
    'Властелин колец: Братство кольца',
    'Матрица',
    'Интерстеллар',
    'Начало',
    'Титаник',
    'Зеленая книга',
    'Побег из Шоушенка',
    'Форрест Гамп',
    'Темный рыцарь'
]

# Запись названий фильмов в файл
write_movies_to_file(filename, movies)

# Чтение содержимого файла и вывод на экран
read_and_print_file(filename)