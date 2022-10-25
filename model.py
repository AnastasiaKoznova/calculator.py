import csv


def csv_data_open():      # 1 - показать все
    with open("csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res

def add_info(list):  # 2- добавление информации
    with open("csv_data.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list[1:])

def del_info(index):  # удаление информации
    list_csv = csv_data_open()
    print(list_csv)
    del list_csv[index]
    with open("csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)

def find_last_name(last_name):  # поиск по фамилии
    list_csv = csv_data_open()
    for i in list_csv:
        if i[0] == last_name:
            print(*i)
            list_find = ' '.join(i)
            return list_find
