def cache_decorator(func):
    cache = None  # Переменная для хранения кешированного результата
    call_count = 0  # Счетчик вызовов
    max_calls = 3  # Число вызовов, после которых кеш обновляется

    def wrapper(*args, **kwargs):
        nonlocal cache, call_count
        if call_count == 0:
            cache = func(*args, **kwargs)  # Вычисление нового результата
            call_count = 1  # Сброс счетчика запросов
            print(f"Кеширован результат (запрос {call_count}/{max_calls})")
        elif call_count < max_calls:
            call_count += 1
            print(f"Используется кешированный результат (запрос {call_count}/{max_calls})")
        else:
            print("\nКеш обновляется...")
            cache = func(*args, **kwargs)  # Вычисление нового результата
            call_count = 1  # Сброс счетчика запросов
            print(f"Кеширован новый результат (запрос {call_count}/{max_calls})")
        return cache

    return wrapper

# Пример использования декоратора
@cache_decorator
def expensive_calculation():
    print("Выполняется операция...")
    return "Операция выполнена"

# Тестирование
print(expensive_calculation())  # Первый запуск, выполняется операция
print(expensive_calculation())  # Второй запуск, используется кеш
print(expensive_calculation())  # Третий запуск, используется кеш
print(expensive_calculation())  # Четвертый запуск, кеш обновляется
print(expensive_calculation())  # Пятый запуск, используется кеш
