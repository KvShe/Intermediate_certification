import datetime


def input_notes():
    lst = [input('Введите название заметки: '), input('Введите текст заметки: ')]
    format_date = '%d.%m.%Y'
    lst.append(datetime.datetime.now().strftime(format_date))
    return lst


def action_request():
    print('''
        1. Создать новую заметку
        2. Вывести все заметки
        3. Вывести заметки по указанной дате
        4. Поиск заметки
        5. Редактировать заметку
        6. Удалить заметку
        7. Выход
        ''')
    return input("Выберите действие: ")


def print_all(dic):
    del dic['id']
    for key, value in dic.items():
        print(value[1] + ': ' + value[2])


def find_by_date(dic):
    date = input('Введите дату в формате "01.01.2023": ')
    del dic['id']
    for key, value in dic.items():
        if value[2] == date:
            print(value[0] + ': ' + value[1])


def find_notes(dic):
    header = input('Введите заголовок искомой заметки: ')
    del dic['id']
    for key, value in dic.items():
        if value[0].find(header) != -1:
            print(value[0] + ': ' + value[1])


def edit_note(dic):
    header = input('Введите заголовок искомой заметки: ')
    id_note = dic['id']
    del dic['id']
    for key, value in dic.items():
        if value[0].find(header) != -1:
            print(value[0] + ': ' + value[1])
            if input('От редактировать эту заметку? Введите "y", если да: ') == 'y':
                dic[key] = input_notes()
                print('Заметка успешно отредактирована')
    dic['id'] = id_note
    return dic


def del_not(dic):
    header = input('Введите заголовок заметки, которую хотите удалить: ')
    id_note = dic['id']
    del dic['id']

    del_note = None
    for key, value in dic.items():
        if value[0].find(header) != -1:
            print(value[0] + ': ' + value[1])
            if input('Удалить эту заметку? Введите "y", если да: ') == 'y':
                del_note = key
                break

    if del_note is not None:
        del dic[del_note]
        print('Заметка удалена')

    dic['id'] = id_note
    return dic
