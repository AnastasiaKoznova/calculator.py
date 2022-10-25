import csv
import os.path

def add_phone_number(f_file, first_name, last_name, number_phone, other):
    if os.path.exists(f_file):
        with open(f_file, mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\n")
            file_writer.writerow([first_name, last_name, number_phone, other])
    else:
        with open(f_file, mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\n")
            file_writer.writerow(["Фамилия", "Имя", "Телефон", "Описание"])
            file_writer.writerow([first_name, last_name, number_phone, other])

def import_phone_number(a_file):
    with open(a_file, 'r', encoding='utf-8') as r_file:
        file_read = r_file.read()
    return file_read