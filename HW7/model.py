import re
import os

def show_dict():
    try:
        with open('phone.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
            if len(file_content) == 0:
                print('Контактов нет')
            else:
                print(file_content)
    except IOError:
        print('Справочник не существует!!!')


def enter_cont():
    id_contact = input('Введите ID контакта: ')
    first_name = input('Введите имя контакта: ')
    last_name = input('Введите фамилию контакта: ')
    phone_number = input('Введите номер телефона: ')
    phone_book = f'{id_contact},{first_name},{last_name},{phone_number}\n'
    with open('phone.txt', 'a+', encoding='utf-8') as file:
        file.write(phone_book)
    print(f'Добавили запись {phone_book}')


def find_cont():
    find = input('Введите имя контакта: ')
    inp = iter(open('phone.txt').readlines())
    for i in inp:
        if find in i:
            print(i)
        else:
            print('Такого контакта нет!')


def del_cont():
    st = input('Введите имя или фамилию: ')
    pattern = re.compile(re.escape(st))
    with open('phone.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)
            file.truncate()


def del_file():
    question = input('Вы уверены? Yes/No: ')
    if question == 'Yes':
        os.remove('phone.txt')