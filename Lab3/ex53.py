import random


# Функция для создания файла с занятостью мест
def create_seating_chart(filename):
    rows = 48 - 18  # Количество рядов
    seats_per_row = 15
    seating_chart = []

    for _ in range(rows):
        row = [random.choice([0, 1]) for _ in range(seats_per_row)]
        seating_chart.append(row)

    # Запись в файл
    with open(filename, "w") as file:
        for row in seating_chart:
            file.write("".join(map(str, row)) + "\n")


# Функция для подсчета свободных мест
def count_free_seats(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    free_count = sum(row.count('0') for row in lines)
    return free_count


# Функция для проверки состояния конкретного места
def check_seat(filename, row_number, seat_number):
    with open(filename, "r") as file:
        lines = file.readlines()

    if row_number < 1 or row_number > len(lines):
        return "Неверный номер ряда"

    row = lines[row_number - 1].strip()
    if seat_number < 1 or seat_number > len(row):
        return "Неверный номер места"

    if row[seat_number - 1] == '0':
        return "Место свободно"
    else:
        return "Место занято"


# Пример использования
if __name__ == "__main__":
    filename = "seating_chart.txt"

    create_seating_chart(filename)

    print(f"Количество свободных мест: {count_free_seats(filename)}")

    row_number = int(input("Введите номер ряда для проверки: "))
    seat_number = int(input("Введите номер места для проверки: "))

    print(check_seat(filename, row_number, seat_number))
