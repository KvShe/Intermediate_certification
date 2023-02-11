import json

file_name = 'counter.json'
# json_data = json.load(open(file_name, encoding='utf-8'))

# Изменение объекта
# json_data['counter'] += 1
# print(type(json_data))
# print(json_data)
#

json_data = {"0": ['header', 'body', 'date']}

json.dump(json_data, open(file_name, mode='w', encoding='utf-8'))
