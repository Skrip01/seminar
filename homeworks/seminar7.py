# Создать телефонный справочник с возможностью импорта и эксоорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.

def load_phonebook(filename):
    phonebook = []  # Инициализация пустого списка для хранения записей телефонного справочника
    try:
        with open(filename, 'r') as file:  # Открытие файла в режиме чтения
            for line in file:  # Чтение файла построчно
                phonebook.append(line.strip().split(','))  # Удаление пробелов и разделение строки по запятой, добавление в список
    except FileNotFoundError:
        pass  # Если файл не найден, программа просто пропускает блок except и возвращает пустой список
    return phonebook  # Возвращение загруженного телефонного справочника


def save_phonebook(phonebook, filename):
    try:
        with open(filename, 'w') as file:  # Открытие файла в режиме записи
            for entry in phonebook:
                file.write(','.join(entry) + '\n')  # Запись каждого элемента телефонного справочника в файл
    except Exception as e:
        print(f"Ошибка при сохранении телефонного справочника: {e}")


def display_phonebook(phonebook):
    if not phonebook:
        print("Телефонный справочник пуст.")
    else:
        for entry in phonebook:
            print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")

def add_entry(phonebook):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phonebook.append([surname, name, patronymic, phone_number])

def search_entry(phonebook, query):
    results = [entry for entry in phonebook if query in entry]
    if not results:
        print("Запись не найдена.")
    else:
        for entry in results:
            print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")

def main():
    filename = 'phonebook.txt'
    phonebook = load_phonebook(filename)

    while True:
        print("\nТелефонный справочник")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Найти запись")
        print("4. Сохранить и выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            display_phonebook(phonebook)
        elif choice == '2':
            add_entry(phonebook)
        elif choice == '3':
            query = input("Введите критерий поиска (имя, фамилия или номер телефона): ")
            search_entry(phonebook, query)
        elif choice == '4':
            save_phonebook(phonebook, filename)
            print("Изменения сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()
