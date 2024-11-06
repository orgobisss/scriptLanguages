# Функция для записи перечня мебели в файл
def write_furniture_to_file(filename, furniture):
    with open(filename, 'w') as file:
        for item in furniture:
            file.write(item + '\n')


# Функция для чтения содержимого файла и вывода на экран
def read_and_print_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


# Укажите имя файла
filename = 'furniture.txt'

# Список мебели
furniture = ['Стол', 'Стул', 'Диван', 'Кровать', 'Шкаф']

# Запись перечня мебели в файл
write_furniture_to_file(filename, furniture)

# Чтение содержимого файла и вывод на экран
read_and_print_file(filename)