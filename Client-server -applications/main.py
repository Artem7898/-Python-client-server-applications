import csv


def get_data():
    files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    result_data = [['Изготовитель системы',
                    'Название ОС', 'Код продукта', 'Тип системы']]
    for file_name in files_list:
        with open('files/' + file_name, encoding='windows-1251') as data_file:
            data = data_file.read().split('\n')
            for i in data:
                row_data = i.split(':')
                if 'Изготовитель системы' in row_data[0]:
                    os_prod_list.append(row_data[1].strip())
                if 'Название ОС' in row_data[0]:
                    os_name_list.append(row_data[1].strip())
                if 'Код продукта' in row_data[0]:
                    os_code_list.append(row_data[1].strip())
                if 'Тип системы' in row_data[0]:
                    os_type_list.append(row_data[1].strip())
                    result_data.append(
                        [
                            os_prod_list[:1][0],
                            os_name_list[:1][0],
                            os_code_list[:1][0],
                            os_type_list[:1][0]
                        ]
                    )

    return result_data


def write_to_csv(file_name):
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        print(get_data())
        for row in get_data():
            csv_writer.writerow(row)

write_to_csv('new_test.csv')
