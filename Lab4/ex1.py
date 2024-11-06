class MinVoda:
    def __init__(self, water_type = None):
        self.water_type = water_type

    def show_my_drink(self):
        if self.water_type in ['столовая', 'лечебная']:
            print(f"Минеральная вода – {self.water_type}")
        else:
            print("Обычная минеральная вода")

# Примеры использования класса
if __name__ == "__main__":
    voda1 = MinVoda("столовая")
    voda1.show_my_drink()  # Вывод: Минеральная вода – Столовая

    voda2 = MinVoda("лечебная")
    voda2.show_my_drink()  # Вывод: Минеральная вода – Лечебная

    voda3 = MinVoda("обычная")
    voda3.show_my_drink()  # Вывод: Обычная минеральная вода