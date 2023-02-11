import gui
from gui import action_request, input_notes, find_by_date, find_notes, edit_note, del_not
from work_whith_json import add, read, write

while True:
    match action_request():
        case '1':
            add(input_notes())
        case '2':
            gui.print_all(read())
        case '3':
            find_by_date(read())
        case '4':
            find_notes(read())
        case '5':
            dic = edit_note(read())
            write(dic)
        case '6':
            dic = del_not(read())
            write(dic)
        case '7':
            print('Приложение завершает работу')
            break
        case _:
            print('Введённая команда не существует')
