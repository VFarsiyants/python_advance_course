"""
Реализовать функцию print_directory_contents(path). Функция принимает имя директории и выводит ее содержимое, включая содержимое всех поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""
import os


def print_directory_contents(dir_name, level=0, remove_git=True):
    cur_instances = (os.listdir(dir_name))
    for item in cur_instances:
        if not item.startswith('.'):
            item_path = os.path.join(dir_name, item)
            if os.path.isdir(item_path):
                print(f'{" " * level}| {item}')
                print_directory_contents(item_path, level+1)
            else:
                print(f'{" "*level}{"-"} {item}')


if __name__ == "__main__":
    print_directory_contents('../')
