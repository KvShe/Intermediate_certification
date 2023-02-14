import datetime


def input_notes(header, body):
    lst = [header, body]
    format_date = '%d.%m.%Y'
    lst.append(datetime.datetime.now().strftime(format_date))
    return lst


def print_all(dic):
    del dic['id']
    for key, value in dic.items():
        print(value[0] + ': ' + value[1] + '\n' + value[2] + '\n')


def find_by_date(date, dic):
    del dic['id']
    for key, value in dic.items():
        if value[2] == date:
            print(value[0] + ': ' + value[1])


def find_notes(header, dic):
    del dic['id']
    for key, value in dic.items():
        if value[0].find(header) != -1:
            print(value[0] + ': ' + value[1])


def edit_note(header, dic):
    id_note = dic['id']
    del dic['id']
    for key, value in dic.items():
        if value[0].find(header) != -1:
            print(value[0] + ': ' + value[1])
            if input('От редактировать эту заметку? Введите "y", если да: ') == 'y':
                dic[key] = input_notes(header, input('Введите текст заметки: '))
                print('Заметка успешно отредактирована')

    dic['id'] = id_note
    return dic


def del_note(header, dic):
    id_note = dic['id']
    del dic['id']

    rm_note = None
    for key, value in dic.items():
        if value[0].find(header) != -1:
            print(value[0] + ': ' + value[1])
            if input('Удалить эту заметку? Введите "y", если да: ') == 'y':
                rm_note = key
                break

    if rm_note is not None:
        del dic[rm_note]
        print('Заметка удалена')

    dic['id'] = id_note
    return dic
