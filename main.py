import sys
from FileHandler import *


# аргумент при запуске - путь к тестовому файлу.


def run_commands(file_handler):
    if file_handler.fileExist:
        print(f'В файле: {file_handler.get_numbers_as_string()}')
        print(f'Минимум: {file_handler.get_min()}')
        print(f'Максимум: {file_handler.get_max()}')
        print(f'Cумма: {file_handler.get_sum()}')
        print(f'Произведение: {file_handler.get_product()}')
    else:
        print("File doesn't exist!")


try:
    path = sys.argv[1]
    file_handler = FileHandler(path)
    run_commands(file_handler)
except IndexError:
    print("You should input argument (path to input) to main file")
