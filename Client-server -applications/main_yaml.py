import yaml

data = {
    '1': ['1', '2', '3'],
    '2': 2,
    '3': {
        '🙏': '1',
        '👍': '2',
        '✍': '3'
    }
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=True, allow_unicode=True)

with open('file.yaml') as f_n:
    yaml_data = yaml.load(f_n, Loader=yaml.FullLoader)

if yaml_data == data:
    print('Данные совпали')
else:
    print('Если не совпали')
