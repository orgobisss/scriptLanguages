# Функция для записи марок автомобилей в файл
def write_car_brands_to_file(filename, car_brands):
    with open(filename, 'w') as file:
        file.write(' - '.join(car_brands))


# Функция для чтения содержимого файла и вывода на экран
def read_and_print_file(filename):
    with open(filename, 'r') as file:
        brand = file.read()
        print(brand)


# Укажите имя файла
filename = 'car_brands.txt'

# Список марок автомобилей
car_brands = ['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes']

# Запись марок автомобилей в файл
write_car_brands_to_file(filename, car_brands)

# Чтение содержимого файла и вывод на экран
read_and_print_file(filename)