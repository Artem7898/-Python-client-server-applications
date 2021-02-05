import yaml

# with open('data_read.yaml') as fn:
#     fn_content = yaml.load(fn)

#     print(fn_content)

#--------------------------------

# Записать в файл:

a_list = ['msg_1', 'msg_2', 'msg_3', 'msg_4']
t_list = ['acc_1', 'acc_2', 'acc_3', 'acc_4']

d_yaml = {'actions': a_list, 'to': t_list}

with open('lesson_yaml.yaml', 'w') as fn:
    yaml.dump(d_yaml, fn) # default_flow_style=False
