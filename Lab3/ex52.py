# Функция для записи стихотворения в файл
def write_poem_to_file(filename, poem):
    with open(filename, 'w') as file:
        file.write(poem)


# Функция для чтения содержимого файла и вывода на экран
def read_and_print_file(filename):
    with open(filename, 'r') as file:
        poem = file.read()
        print(poem)
        return poem


# Функция для подсчета слов по первой букве
def count_words_by_first_letter(poem):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'  # Гласные буквы
    consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'  # Согласные буквы

    vowel_count = 0
    consonant_count = 0

    words = poem.split()  # Разделяем стихотворение на слова

    for word in words:
        first_letter = word[0]  # Берем первую букву слова
        if first_letter in vowels:
            vowel_count += 1
        elif first_letter in consonants:
            consonant_count += 1

    return vowel_count, consonant_count


# Укажите имя файла
filename = 'poem.txt'

# Стихотворение (пример)
poem = """  
Однажды в студёную зимнюю нору 
Охотник свалился, теряя опору. 
— Мне что же, — ворчит, — до весны здесь сидеть?! 
— Да ты оптимист! — отозвался медведь.
"""

# Запись стихотворения в файл
write_poem_to_file(filename, poem)

# Чтение содержимого файла и вывод на экран
read_and_print_file(filename)

# Подсчет слов по первой букве
vowel_count, consonant_count = count_words_by_first_letter(poem)

# Вывод результатов подсчета
if vowel_count > consonant_count:
    print(f"\nБольше слов на гласную: {vowel_count} (гласные), {consonant_count} (согласные)")
elif consonant_count > vowel_count:
    print(f"\nБольше слов на согласную: {consonant_count} (согласные), {vowel_count} (гласные)")
else:
    print(f"\nКоличество слов одинаковое: {vowel_count} (гласные), {consonant_count} (согласные)")