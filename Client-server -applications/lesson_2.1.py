import json

# with open('mes_example_read.json') as fn:
#     str_obj = fn.read()
#     objs = json.loads(str_obj)
#     print(objs)

# for key, value in objs.items():
#    print(key, value)
# ---------------------------------------------------


# Запись в файл JSON:


dict_to_Json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}

with open('lesson_2.py.json', 'w') as fn:
    # fn.write(json.dumps(dict_to_json))
    json.dump(dict_to_Json, fn, sort_keys=True, indent=4)
