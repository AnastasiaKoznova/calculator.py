def input_numbers():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    number_phone = input("Введите номер телефона: ")
    other = input("Введите примечание: ")
    list_n = [first_name, last_name, number_phone, other]
    return list_n

def input_name_file():
    f_file = input("Введите название и формат файла (например: file.txt или file.csv): ")
    return f_file

def output_name_file():
    out_file = input("Введите название и расширение файла для прочтения: ")
    return out_file

def what_to_do():
    to_do = int(input("Введите номер действия: 1 - Импортировать данные в файл, 2 - Экспортировать данные из файла: "))
    return to_do

def new_input():
    new_in = input("Повторить ввод данных? (Yes/No): ")
    return new_in

