"""
Написать программу, в которой реализовать две функции. В первой должен 
создаваться простой текстовый файл. Если файл с таким именем уже существует, 
выводим соответствующее сообщение и завершаем работу. Необходимо открыть файл и 
создать два списка: с текстовой и числовой информацией. Для создания списков 
использовать генераторы. Применить к спискам функцию zip(). Результат 
выполнения этой функции должен должен быть обработан и записан в файл таким 
образом, чтобы каждая строка файла содержала текстовое и числовое значение 
(например example345). Вызвать вторую функцию. В нее должна передаваться ссылка 
на созданный файл. Во второй функции необходимо реализовать открытие файла и 
простой, построчный вывод содержимого. 
"""
import os


def write_file(filename):
    if filename in os.listdir():
        print(f'файл {filename} уже существует')
    keys = (key for key in ['example', 'wong', 'monkey', 'lu'])
    vals = (val for val in [12, 92, 40, 37])
    with open(filename, 'w', encoding='utf-8') as f:
        for key, val in zip(keys, vals):
            f.write(f'{key}{val}\n')

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.replace('\n', ''))


if __name__ == '__main__':
    test_filename = 'test'
    write_file(test_filename)
    read_file(test_filename)
