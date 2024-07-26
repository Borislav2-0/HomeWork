# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name -
# название файла для записи, strings - список строк для записи.
# Функция должна:
#     Записывать в файл file_name все строки из списка strings, каждая на новой строке.
#     Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
#   а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
#   {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
#   1, 2 - номера записанных строк.
#   0, 16 - номера байт, на которых началась запись строк.
#   'Text for tell.', 'Используйте кодировку utf-8.' - сами строки

from pprint import pprint


def custom_write(file_name, strings):
    strings_position = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            st_pos = file.tell()
            file.write(string + '\n')
            strings_position[(len(strings_position) + 1, st_pos)] = string
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

res = custom_write('test.txt', info)
for el in res.items():
    print(el)
