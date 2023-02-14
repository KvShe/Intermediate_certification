from gui import show_menu, continue_to_work, input_date, input_header, input_body, exit_app
from work_whith_json import add, read, write
from model import input_notes, print_all, find_by_date, find_notes, edit_note, del_note


def main():
    while True:
        match show_menu():
            case '1':
                add(input_notes(input_header(), input_body()))
            case '2':
                print_all(read())
                continue_to_work()
            case '3':
                find_by_date(input_date(), read())
                continue_to_work()
            case '4':
                find_notes(input_header(), read())
            case '5':
                dic = edit_note(input_header(), read())
                write(dic)
            case '6':
                dic = del_note(input_header(), read())
                write(dic)
            case '7':
                exit_app()
                break
            case _:
                print('Введённая команда не существует')
