import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('lesson_2_py.csv', 'w') as fn:
    fn_write = csv.writer(fn, quoting=csv.QUOTE_NONNUMERIC) # delimiter='#' указывать при чтении:
    fn_write.writerows(data) # Без перебора массива:
#     for row in data:
#         fn_write.writerow(row)
