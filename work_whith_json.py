import json

from config import name_file


def read():
    with open(name_file, 'r') as file:
        return json.load(file)


def write(dic):
    with open(name_file, 'w') as file:
        json.dump(dic, file, indent=4)
        file.close()


def add(lst):
    dic = read()
    id_note = dic['id'] + 1

    dic[id_note] = lst
    dic['id'] = id_note
    write(dic)
    print('Запись добавлена')
